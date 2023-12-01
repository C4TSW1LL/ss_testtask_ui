import pytest

from .pages.base_methods import BaseMethods
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from .pages.disk_page import DiskPage


def pytest_addoption(parser):
    parser.addoption("--browser", default="chrome")
    parser.addoption("--url", default="https://ya.ru/")


@pytest.fixture()
def browser(request):
    browser = request.config.getoption("--browser")
    url = request.config.getoption("--url")

    if browser == "chrome":
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    elif browser == "firefox":
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    else:
        raise Exception("Браузер не поддерживается")

    driver.implicitly_wait(3)
    driver.maximize_window()
    driver.get(request.config.getoption("--url"))
    yield driver
    driver.quit()



@pytest.fixture()
def logout(browser):
    yield
    DiskPage(browser).logout()
    BaseMethods.api_delete_tests_file()
