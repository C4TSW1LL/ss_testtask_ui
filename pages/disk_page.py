from .locators import DiskPageLocators
from .base_methods import BaseMethods
from selenium.common import TimeoutException
from selenium.webdriver.common.keys import Keys


class DiskPage(BaseMethods):
    def __init__(self, driver):
        super().__init__(driver)

    def create_docs_file(self, file_name):
        self.click(*DiskPageLocators.CREATE_BTN)
        self.click(*DiskPageLocators.CREATE_TEXT_DOC_BTN)
        while self.find_element(*DiskPageLocators.INPUT_NAME_FIELD).get_attribute('value') != '':
            self.find_element(*DiskPageLocators.INPUT_NAME_FIELD).send_keys(Keys.BACK_SPACE)
        self.input_value(*DiskPageLocators.INPUT_NAME_FIELD, file_name)
        self.click(*DiskPageLocators.CREATE_SUBMIT_BTN)
        self.close_window()

    def create_folder(self, folder_name):
        self.click(*DiskPageLocators.CREATE_BTN)
        self.click(*DiskPageLocators.CREATE_FOLDER_BTN)
        while self.find_element(*DiskPageLocators.INPUT_NAME_FIELD).get_attribute('value') != '':
            self.find_element(*DiskPageLocators.INPUT_NAME_FIELD).send_keys(Keys.BACK_SPACE)
        self.input_value(*DiskPageLocators.INPUT_NAME_FIELD, folder_name)
        self.click(*DiskPageLocators.CREATE_SUBMIT_BTN)

    def open_by_double_click(self, file_name):
        self.double_click(self.find_element(*DiskPageLocators.folder(file_name)))

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

    def upload_file(self, name):
        self.call_context_menu()
        self.create_txt_file(self, name)
        self.find_element(*DiskPageLocators.UPLOAD_BTN).send_keys(f'data/{name}')