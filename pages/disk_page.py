from .locators import DiskPageLocators
from .base_methods import BaseMethods
from selenium.common import TimeoutException
from selenium.webdriver.common.keys import Keys


class DiskPage(BaseMethods):
    def __init__(self, driver):
        super().__init__(driver)

    def create_docs_file(self, file_name):
        try:
            self.click(*DiskPageLocators.CREATE_BTN)
            self.click(*DiskPageLocators.CREATE_TEXT_DOC_BTN)
            if self.find_element(*DiskPageLocators.INPUT_NAME_FIELD).get_attribute('value') != '':
                self.find_element(*DiskPageLocators.INPUT_NAME_FIELD).send_keys(Keys.BACK_SPACE)
            self.input_value(*DiskPageLocators.INPUT_NAME_FIELD, file_name)
            self.click(*DiskPageLocators.CREATE_SUBMIT_BTN)
            self.close_window()
        except TimeoutException:
            print("Ошибка в создании текстового файла")

    def create_folder(self, folder_name):
        try:
            self.click(*DiskPageLocators.CREATE_BTN)
            self.click(*DiskPageLocators.CREATE_FOLDER_BTN)
            if self.find_element(*DiskPageLocators.INPUT_NAME_FIELD).get_attribute('value') != '':
                self.find_element(*DiskPageLocators.INPUT_NAME_FIELD).send_keys(Keys.BACK_SPACE)
                # self.find_element(*DiskPageLocators.INPUT_NAME_FIELD).clear()
            self.input_value(*DiskPageLocators.INPUT_NAME_FIELD, folder_name)
            self.click(*DiskPageLocators.CREATE_SUBMIT_BTN)
        except TimeoutException:
            print("Ошибка в создании папки")

    def open(self, file_name):
        try:
            self.double_click(file_name)
        except TimeoutException:
            print("Не удалось открыть")

    def check_file_name(self, file_name):
        try:
            element = self.driver.find_element(*DiskPageLocators.docx_file(file_name))
            return element.get_attribute("aria-label")
        except TimeoutException:
            print("Файл с таким именем не найден")

    def check_file_is_created(self, file_name):
        return self.check_element(*DiskPageLocators.docx_file(file_name))

    def logout(self):
        self.click(*DiskPageLocators.AVATAR_BTN)
        self.click(*DiskPageLocators.LOGOUT_BTN)
