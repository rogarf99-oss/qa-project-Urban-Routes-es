from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from urban_routes_page import UrbanRoutesPage


def main():
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    chrome_options.set_capability("goog:loggingPrefs", {"performance": "ALL"})
    driver = webdriver.Chrome(options=chrome_options)

    try:
        page = UrbanRoutesPage(driver)
        page.open()
        page.set_route()
        page.select_comfort()
        page.enter_phone_number_and_request_code()
        page.enter_and_confirm_sms_code()
        page.add_payment_method()

        assert "Comfort" in driver.page_source
        print("Flujo completo ejecutado correctamente.")

    except Exception as e:
        print(f"Error en la prueba: {e}")

    finally:
        driver.quit()


if __name__ == "__main__":
    main()
