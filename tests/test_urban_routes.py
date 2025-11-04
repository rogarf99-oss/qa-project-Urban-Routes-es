import pytest
from pages.urban_routes_page import UrbanRoutesPage

class TestUrbanRoutes:

    def test_full_request_flow_with_sms_and_card(self, driver):
        page = UrbanRoutesPage(driver)
        page.open()

        page.set_route()

        page.select_comfort()

        page.enter_phone_number_and_request_code("+1 123 123 12 12")

        page.enter_and_confirm_sms_code()

        page.add_payment_method()

        assert "Comfort" in driver.page_source