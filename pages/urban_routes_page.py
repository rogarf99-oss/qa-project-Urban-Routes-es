import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from configuration import BASE_URL
from data import FROM_ADDRESS, TO_ADDRESS, PHONE_NUMBER, CARD_NUMBER, CARD_CODE
from utils.phone_intercept import retrieve_phone_code
from selenium.webdriver import ActionChains


class UrbanRoutesPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = BASE_URL

        self.input_from = (By.ID, "from")
        self.input_to = (By.ID, "to")
        self.button_order_taxi = (By.CSS_SELECTOR, "button.button.round")

        self.tariff_comfort = (By.XPATH, "//div[@class='tcard-title' and text()='Comfort']")

        self.phone_step_button = (By.CSS_SELECTOR, "div.np-button")
        self.input_phone = (By.ID, "phone")
        self.button_next = (By.XPATH, "//button[text()='Siguiente']")

        self.input_code = (By.ID, "code")
        self.button_confirm = (By.XPATH, "//button[text()='Confirmar']")

        self.payment_method_arrow = (By.CSS_SELECTOR, "img[alt='Arrow right']")
        self.add_payment_button = (By.CSS_SELECTOR, "img.pp-plus[alt='plus']")
        self.input_card_number = (By.ID, "number")
        self.input_card_code = (By.ID, "code")  # mismo id, contexto diferente (tarjeta)
        self.placeholder_click_area = (By.CSS_SELECTOR, "div.plc")
        self.button_add_card = (By.CSS_SELECTOR, "button.button.full")
        self.button_close_payment = (By.CSS_SELECTOR, "button.close-button.section-close")

    def open(self):
        self.driver.get(self.url)
        time.sleep(1)

    def set_from_address(self):
        wait = WebDriverWait(self.driver, 20)
        el = wait.until(EC.visibility_of_element_located(self.input_from))
        el.clear()
        time.sleep(0.5)
        el.send_keys(FROM_ADDRESS)
        time.sleep(0.5)

    def set_to_address(self):
        wait = WebDriverWait(self.driver, 20)
        el = wait.until(EC.visibility_of_element_located(self.input_to))
        el.clear()
        time.sleep(0.5)
        el.send_keys(TO_ADDRESS)
        time.sleep(0.5)

    def click_order_taxi(self):
        wait = WebDriverWait(self.driver, 20)
        btn = wait.until(EC.element_to_be_clickable(self.button_order_taxi))
        time.sleep(0.5)
        btn.click()
        time.sleep(1)

    def set_route(self):
        self.set_from_address()
        self.set_to_address()
        self.click_order_taxi()

    def select_comfort(self):
        wait = WebDriverWait(self.driver, 20)
        btn = wait.until(EC.element_to_be_clickable(self.tariff_comfort))
        time.sleep(0.5)
        btn.click()
        time.sleep(1)

    def enter_phone_number_and_request_code(self, phone_number=PHONE_NUMBER):
        wait = WebDriverWait(self.driver, 20)
        phone_btn = wait.until(EC.element_to_be_clickable(self.phone_step_button))
        time.sleep(0.5)
        phone_btn.click()
        time.sleep(0.5)

        phone_input = wait.until(EC.visibility_of_element_located(self.input_phone))
        phone_input.clear()
        time.sleep(0.3)
        phone_input.send_keys(phone_number)
        time.sleep(0.5)

        next_btn = wait.until(EC.element_to_be_clickable(self.button_next))
        time.sleep(0.5)
        next_btn.click()
        time.sleep(2)

    def enter_and_confirm_sms_code(self):
        wait = WebDriverWait(self.driver, 30)
        code = retrieve_phone_code(self.driver)
        code_input = wait.until(EC.visibility_of_element_located(self.input_code))
        code_input.clear()
        time.sleep(0.3)
        code_input.send_keys(code)
        time.sleep(0.5)

        confirm_btn = wait.until(EC.element_to_be_clickable(self.button_confirm))
        time.sleep(0.5)
        confirm_btn.click()
        time.sleep(1)

    def add_payment_method(self):
        wait = WebDriverWait(self.driver, 20)
        actions = ActionChains(self.driver)

        arrow_btn = wait.until(EC.element_to_be_clickable(self.payment_method_arrow))
        arrow_btn.click()
        time.sleep(1)

        add_btn = wait.until(EC.element_to_be_clickable(self.add_payment_button))
        add_btn.click()
        time.sleep(1)

        card_code = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input.card-input#code")))
        card_code.clear()
        card_code.send_keys(CARD_CODE)
        time.sleep(1)

        card_number = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input.card-input#number")))
        card_number.clear()
        card_number.send_keys(CARD_NUMBER)
        time.sleep(1)

        try:
            head_div = self.driver.find_element(By.CSS_SELECTOR, "div.head")
            head_div.click()
        except:
            actions.move_by_offset(10, 10).click().perform()
        time.sleep(2)

        add_card_btn = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "button.button.full")))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", add_card_btn)
        time.sleep(1)

        is_disabled = self.driver.execute_script("return arguments[0].disabled;", add_card_btn)
        if not is_disabled:
            try:
                wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.button.full")))
                actions.move_to_element(add_card_btn).pause(0.3).click().perform()
            except:
                self.driver.execute_script("arguments[0].click();", add_card_btn)
        else:
            self.driver.execute_script("arguments[0].click();", add_card_btn)
        time.sleep(3)

        try:
            close_btn = wait.until(EC.element_to_be_clickable(self.button_close_payment))
            close_btn.click()
            time.sleep(1)
        except Exception as e:
            print(f"ADVERTENCIA: No se pudo cerrar la ventana de métodos de pago: {e}")

        try:
            comment_input = wait.until(EC.visibility_of_element_located((By.ID, "comment")))
            comment_input.clear()
            time.sleep(0.5)
            comment_input.send_keys("Traiga un aperitivo")
            time.sleep(2)
            print("DEBUG: Mensaje agregado correctamente.")
        except Exception as e:
            print(f"ADVERTENCIA: No se pudo agregar el mensaje: {e}")

        try:
            slider_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "span.slider.round")))
            slider_btn.click()
            time.sleep(2)
            print("DEBUG: Se seleccionó manta y pañuelos.")
        except Exception as e:
            print(f"ADVERTENCIA: No se pudo seleccionar manta y pañuelos: {e}")

        try:
            counter_plus_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div.counter-plus")))
            counter_plus_btn.click()
            time.sleep(1)
            counter_plus_btn.click()
            time.sleep(2)
            print("DEBUG: Se agregaron dos helados correctamente.")
        except Exception as e:
            print(f"ADVERTENCIA: No se pudieron agregar los helados: {e}")

        try:
            smart_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "span.smart-button-secondary")))
            smart_button.click()
            print("DEBUG: Se presionó el botón de recorrido correctamente.")
            time.sleep(10)  # esperar 10 segundos en pantalla
        except Exception as e:
            print(f"ADVERTENCIA: No se pudo presionar el botón de recorrido: {e}")

        print("DEBUG: Flujo completo ejecutado. Página queda abierta para cierre manual.")