import pytest
from pages.urban_routes_page import UrbanRoutesPage

@pytest.mark.usefixtures("driver")
class TestUrbanRoutes:
    @pytest.fixture(autouse=True)
    def setup(self, driver):
        self.page = UrbanRoutesPage(driver)
        self.page.open()

    def test_01_set_route(self):
        """01. Confirmación del establecimiento de la ruta"""
        self.page.set_route()
        assert "Comfort" in self.page.driver.page_source

    def test_02_select_comfort(self):
        """02. Verifica que se selecciona la tarifa Comfort"""
        self.page.select_comfort()
        assert "Comfort" in self.page.driver.page_source

    def test_03_enter_phone_number(self):
        """03. Prueba que verifica que se ingrese número de teléfono"""
        self.page.enter_phone_number_and_request_code()
        assert "Confirmar" in self.page.driver.page_source

    def test_04_enter_and_confirm_sms_code(self):
        """04. Prueba que verifica el ingreso del código SMS"""
        self.page.enter_and_confirm_sms_code()
        assert "Método de pago" in self.page.driver.page_source or "Tarjeta" in self.page.driver.page_source

    def test_05_add_payment_method(self):
        """05. Prueba que agrega tarjeta de crédito"""
        self.page.add_payment_method()
        assert "Tarjeta" in self.page.driver.page_source or "Método de pago" in self.page.driver.page_source

    def test_06_write_message(self):
        """06. Prueba que escribe mensaje para el conductor"""
        input_message = self.page.driver.find_element("id", "comment")
        input_message.clear()
        input_message.send_keys("Muéstrame el camino al museo")
        assert "Muéstrame el camino" in input_message.get_attribute("value")

    def test_07_blanket(self):
        """07. Prueba que solicita una frazada"""
        blanket_switch = self.page.driver.find_element("id", "blanket")
        blanket_switch.click()
        assert blanket_switch.is_selected()

    def test_08_add_icecream(self):
        """08. Prueba que añade helados"""
        icecream_switch = self.page.driver.find_element("id", "icecream")
        icecream_switch.click()
        assert icecream_switch.is_selected()

    def test_09_find_driver(self):
        """09. Prueba que verifica la búsqueda de un conductor"""
        assert "Buscando conductor" in self.page.driver.page_source or "Conductor encontrado" in self.page.driver.page_source