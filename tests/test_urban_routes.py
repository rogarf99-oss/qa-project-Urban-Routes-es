# tests/test_urban_routes.py
import pytest
from fixtures.driver import driver
from pages.urban_routes_page import UrbanRoutesPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture(autouse=True)
def setup_page(request, driver):
    request.cls.driver = driver
    request.cls.page = UrbanRoutesPage(driver)


@pytest.mark.usefixtures("setup_page")
class TestUrbanRoutes:

    def test_01_set_route(self):
        """01. Confirmación del establecimiento de la ruta"""
        self.page.set_route()
        assert "Comfort" in self.page.driver.page_source

    def test_02_select_comfort(self):
        """02. Verifica que se selecciona la tarifa Comfort"""
        self.page.select_comfort()
        assert "Número de teléfono" in self.page.driver.page_source

    def test_03_enter_phone(self):
        """03. Ingreso y confirmación del número de teléfono"""
        self.page.enter_phone()

        self.page.wait.until(
            EC.invisibility_of_element_located((By.CSS_SELECTOR, "div.np-button-modal"))
        )
        print("✓ Número de teléfono confirmado correctamente")

    def test_04_add_card(self):
        """04. Agregar tarjeta de crédito"""
        self.page.add_card()
        print("✓ Tarjeta agregada correctamente")

    def test_05_write_comment(self):
        """05. Escribir un mensaje para el conductor"""
        self.page.write_comment()
        assert "Muéstrame el camino" in self.page.driver.page_source

    def test_06_select_blanket(self):
        """06. Pedir una manta y pañuelos"""
        self.page.select_blanket()

    def test_07_add_icecreams(self):
        """07. Pedir dos helados"""
        self.page.add_icecreams()

        # Esperamos a que el label de Helado esté presente antes de validar
        wait = WebDriverWait(self.page.driver, 10)
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.r-counter-label")))
        assert "Helado" in self.page.driver.page_source

    def test_08_wait_for_driver(self):
        """08. Esperar modal de búsqueda de taxi"""
        self.page.wait_for_driver()
        assert "Buscar automóvil" in self.page.driver.page_source