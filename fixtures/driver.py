from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import pytest


@pytest.fixture(scope="session")
def driver():

    options = Options()
    options.add_argument("--start-maximized")
    options.add_argument("--disable-infobars")
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-notifications")
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    options.set_capability("goog:loggingPrefs", {"performance": "ALL"})

    service = Service()
    driver = webdriver.Chrome(service=service, options=options)

    # navegador abierto toda la sesión
    yield driver

    driver.quit()