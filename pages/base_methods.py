from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from .locators import DiskPageLocators
import requests


class BaseMethods:
    def __init__(self, driver):
        self.driver = driver
        self.action = ActionChains(self.driver)

    def find_element(self, by: By, selector: str, timeout=5):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located((by, selector)), message=f'No such element {selector}')

    def check_element(self, by: By, selector: str):
        """
        Обертка над WebDriverWait и expected_condition. Поиск элемента,
        который отобразился не только
        в DOM дереве, но и имеет высоту/ширину - явно отобразился на странице.
        """
        try:
            self.find_element(by, selector)
            return WebDriverWait
        except TimeoutException:
            return False

    def click(self, by, selector: str):
        self.find_element(by, selector).click()

    def double_click(self, element):
        try:
            self.action.double_click(element).perform()
        except TimeoutException:
            return f'No such element {element}'

    def call_context_menu(self):
        try:
            self.action.context_click(*DiskPageLocators.CONTEXT_FIELD).perform()
        except TimeoutException:
            return f'No such element {DiskPageLocators.CONTEXT_FIELD}'

    def input_value(self, by, selector: str, value):
        self.find_element(by, selector).send_keys(value)

    def close_window(self):
        self.driver.switch_to.window(self.driver.window_handles[-1])
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[1])

    @staticmethod
    def api_delete_tests_file():
        delete_url = "https://cloud-api.yandex.net/v1/disk/resources?path=TestFolder&permanently=true"
        headers = {'Authorization': 'OAuth y0_AgAAAAByb1ODAADLWwAAAADzbOpmCEE7bzh2Swq1KU1x5Gl1vooS0gA'}
        requests.request("DELETE", url=delete_url, headers=headers)

    '''TO DO'''

    def create_txt_file(self, name: str):
        with open(name, "w+") as f:
            f.write("The text to check")


