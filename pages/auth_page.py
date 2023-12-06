from .locators import AuthPageLocators
from .base_methods import BaseMethods
from data.verification_data import VerData


class AuthPage(BaseMethods):
    def __init__(self, driver):
        super().__init__(driver)

    def login(self):
        self.click(*AuthPageLocators.AUTH_BTN)
        self.click(*AuthPageLocators.LOGIN_BY_EMAIL_BTN)
        self.input_value(*AuthPageLocators.LOGIN_FIELD, VerData.LOGIN)
        self.click(*AuthPageLocators.SING_IN_BTN)
        self.input_value(*AuthPageLocators.PASSWORD_FIELD, VerData.PASSWORD)
        self.click(*AuthPageLocators.SING_IN_BTN)
        if self.check_element(*AuthPageLocators.CLOSE_ALERT_BUTTON):
            self.click(*AuthPageLocators.CLOSE_ALERT_BUTTON)
        else:
            pass

    def open_disk_page(self):
        self.click(*AuthPageLocators.AVATAR_BTN)
        '''Смена таргета селениума на фрейм с меню'''
        self.driver.switch_to.frame(self.driver.find_element(*AuthPageLocators.USER_MENU_FRAME))
        self.click(*AuthPageLocators.DISK_BTN)
        self.driver.switch_to.window(self.driver.window_handles[1])
