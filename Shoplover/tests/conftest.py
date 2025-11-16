from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
import pytest
from selenium import webdriver
import time


def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default="Edge")


@pytest.fixture(scope="class")
def setup(request):
    browser_name = request.config.getoption("browser_name")

    if browser_name == "Edge":
        service = EdgeService(r"C:\Users\USER\PycharmProjects\Shoplover\Drivers\msedgedriver.exe")
        driver = webdriver.Edge(service=service)

    elif browser_name == "firefix":
        service = FirefoxService(r"C:\Users\USER\PycharmProjects\Shoplover\Drivers\geckodriver.exe")
        driver = webdriver.Firefox(service=service)

    elif browser_name == "Chrome":
        service = ChromeService(r"C:\Users\USER\PycharmProjects\Shoplover\Drivers\chromedriver.exe")
        driver = webdriver.Chrome(service=service)

    driver.implicitly_wait(5)
    driver.maximize_window()
    driver.get("https://cartup.com/")

    request.cls.driver = driver
    yield
    time.sleep(2)
    driver.quit()
