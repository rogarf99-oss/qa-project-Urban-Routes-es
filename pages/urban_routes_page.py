from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from utils.phone_intercept import retrieve_phone_code
import data
import time


class UrbanRoutesPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://cnt-6778d7f8-c8e5-410b-955b-f820d2657a85.containerhub.tripleten-services.com?lng=es"
        self.wait = WebDriverWait(self.driver, 15)

        # --- Selectores ---
        self.from_field = (By.CSS_SELECTOR, '[id="from"]')
        self.to_field = (By.CSS_SELECTOR, '[id="to"]')
        self.route_button = (By.CSS_SELECTOR, '[id="from"] + div button')
        self.order_button_round = (By.CSS_SELECTOR, 'button.button.round')

        self.comfort_tariff = (By.CSS_SELECTOR, '.tcard:nth-child(3)')
        self.phone_field = (By.CSS_SELECTOR, '[name="phone"]')
        self.next_button = (By.CSS_SELECTOR, '[id="next"]')
        self.sms_code_field = (By.CSS_SELECTOR, '[name="code"]')
        self.add_card_button = (By.CSS_SELECTOR, '[id="card"]')
        self.comment_field = (By.CSS_SELECTOR, '[name="comment"]')
        self.blanket_checkbox = (By.CSS_SELECTOR, '[for="blanket"]')
        self.icecream_plus = (By.CSS_SELECTOR, '[data-testid="plus"]')
        self.final_order_button = (By.CSS_SELECTOR, '[id="order-button"]')

    # --- Métodos de acción ---

    def open(self):
        """Abre la página base"""
        self.driver.get(self.url)
        time.sleep(2)

    def set_route(self):
        """01. Establece la ruta y pide un taxi"""
        self.open()

        from_input = self.wait.until(EC.presence_of_element_located(self.from_field))
        from_input.clear()
        from_input.send_keys(data.address_from)

        to_input = self.wait.until(EC.presence_of_element_located(self.to_field))
        to_input.clear()
        to_input.send_keys(data.address_to)

        # Espera botón “Pedir un taxi”
        pedir_btn = self.wait.until(EC.element_to_be_clickable(self.order_button_round))
        pedir_btn.click()
        time.sleep(2)

    def select_comfort(self):
        """02. Selecciona la tarifa Comfort"""
        comfort_option = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//div[@class='tcard-title' and text()='Comfort']"))
        )
        comfort_option.click()
        time.sleep(1)

    def enter_phone(self):
        """03. Ingreso y confirmación del número de teléfono"""
        print("→ Ingresando número de teléfono...")

        # Hacer clic en el botón para abrir el modal de teléfono
        phone_btn = self.wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "div.np-button div.np-text")
        ))
        phone_btn.click()
        print("✓ Modal de teléfono abierto")

        # Ingresar el número de teléfono
        phone_input = self.wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, "input#phone")
        ))
        phone_input.clear()
        phone_input.send_keys("+1 123 123 12 12")
        print("✓ Número ingresado")

        # Clic en “Siguiente”
        next_btn = self.wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "button.button.full[type='submit']"))
        )
        next_btn.click()
        print("→ Botón 'Siguiente' presionado")

        # Interceptar código SMS
        sms_code = retrieve_phone_code(self.driver)
        print(f"✓ Código interceptado: {sms_code}")

        # Ingresar el código
        code_input = self.wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, "input#code")
        ))
        code_input.clear()
        code_input.send_keys(sms_code)
        print("✓ Código ingresado")

        # Esperar y hacer clic en Confirmar
        confirm_btn = self.wait.until(EC.element_to_be_clickable(
            (By.XPATH,
             "//button[@type='submit' and contains(@class,'button') and contains(@class,'full') and text()='Confirmar']")
        ))
        confirm_btn.click()
        print("✓ Botón 'Confirmar' clickeado")

        time.sleep(1)

    def add_card(self):
        print("→ Agregando una tarjeta de crédito...")
        wait = WebDriverWait(self.driver, 20)
        actions = ActionChains(self.driver)

        # Elegir método de pago
        method_button = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//img[@alt='Arrow right']"))
        )
        method_button.click()
        print("✓ Método de pago seleccionado")
        time.sleep(1)

        # Abrir modal “Agregar método de pago”
        add_method = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//img[@alt='plus']"))
        )
        add_method.click()
        print("✓ Modal 'Agregar método de pago' abierto")
        time.sleep(1)

        # Ingresar código de tarjeta (CVV)
        card_code = wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "input.card-input#code"))
        )
        self.driver.execute_script("arguments[0].scrollIntoView(true);", card_code)
        card_code.clear()
        card_code.send_keys("111")  # código de ejemplo
        print("✓ Código de tarjeta ingresado")
        time.sleep(0.5)

        # Ingresar número de tarjeta
        card_number = wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "input.card-input#number"))
        )
        self.driver.execute_script("arguments[0].scrollIntoView(true);", card_number)
        card_number.clear()
        card_number.send_keys("1234 5678 9100")  # número de ejemplo
        print("✓ Número de tarjeta ingresado")
        time.sleep(0.5)

        # Cambiar foco para habilitar el botón 'Agregar'
        try:
            head_div = self.driver.find_element(By.CSS_SELECTOR, "div.head")
            head_div.click()
        except:
            # Si falla, enviar TAB al campo CVV
            card_code.send_keys(Keys.TAB)
        time.sleep(0.5)

        # Forzar clic en el botón “Agregar”
        add_card_btn = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "button.button.full")))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", add_card_btn)
        time.sleep(0.5)
        try:
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.button.full")))
            actions.move_to_element(add_card_btn).click().perform()
        except:
            self.driver.execute_script("arguments[0].click();", add_card_btn)

        print("✓ Tarjeta confirmada correctamente")
        time.sleep(1)

    def write_comment(self, message="Muéstrame el camino"):
        """05. Escribir un mensaje para el conductor"""
        print("→ Escribiendo comentario para el conductor...")

        # Esperar a que el input del comentario sea visible
        comment_input = self.wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "input#comment.input"))
        )

        # Hacer scroll si es necesario
        self.driver.execute_script("arguments[0].scrollIntoView(true);", comment_input)

        # Limpiar y enviar el mensaje
        comment_input.clear()
        comment_input.send_keys(message)
        print(f"✓ Comentario ingresado: {message}")

        # Confirmar envío (Enter o clic fuera)
        comment_input.send_keys(Keys.ENTER)
        time.sleep(0.5)
        print("✓ Comentario enviado")

    def select_blanket(self):
        print("→ Seleccionando manta y pañuelos...")
        wait = WebDriverWait(self.driver, 10)

        # Localizamos el switch
        switch = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "span.slider.round")))

        # Hacemos clic usando JS para evitar errores de interceptación
        self.driver.execute_script("arguments[0].click();", switch)
        time.sleep(0.5)

        # Validamos que el texto "Manta y pañuelos" esté visible
        label = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.r-sw-label")))
        assert "Manta y pañuelos" in label.text
        print("✓ Manta y pañuelos seleccionados correctamente")

    def add_icecreams(self):
        print("→ Agregando 2 helados...")
        wait = WebDriverWait(self.driver, 10)

        # Localizamos el botón "más" de helado
        plus_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div.counter-plus")))

        # Hacemos clic 2 veces
        for _ in range(2):
            self.driver.execute_script("arguments[0].click();", plus_button)
            time.sleep(0.3)

        # Validamos que el label "Helado" esté visible
        label = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.r-counter-label")))
        assert "Helado" in label.text
        print("✓ 2 helados agregados correctamente")

    def wait_for_driver(self):
        print("→ Solicitando un taxi...")
        wait = WebDriverWait(self.driver, 20)

        # Esperar a que desaparezca el overlay si existe
        try:
            overlay = self.driver.find_element(By.CSS_SELECTOR, "div.overlay")
            wait.until(EC.invisibility_of_element(overlay))
            print("✓ Overlay desapareció")
        except:
            # Si no existe, seguimos
            pass

        # Esperar a que el botón "Pedir un taxi" sea clickable
        taxi_button = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button.smart-button"))
        )
        taxi_button.click()
        print("✓ Botón 'Pedir un taxi' clickeado")

        # Esperar a que aparezca la pantalla de búsqueda de automóvil
        print("→ Esperando pantalla de 'Buscar automóvil'...")
        wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "div.order-header-title"))
        )
        print("✓ Pantalla 'Buscar automóvil' visible")

        # Mantener la pantalla visible 10 segundos
        print("→ Manteniendo pantalla 10 segundos...")
        time.sleep(10)