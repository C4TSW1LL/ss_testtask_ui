from selenium.webdriver.common.by import By


class CapchaPageLocators:
    ASSERT_CAPCHA_BTN = (By.CSS_SELECTOR, "input[type='submit']")


class AuthPageLocators:
    AUTH_BTN = (By.XPATH, "//a[contains(@href, 'https://passport.yandex.ru/auth?retpath')]")
    LOGIN_BY_EMAIL_BTN = (By.CSS_SELECTOR, "button[data-type='login']")
    LOGIN_FIELD = (By.CSS_SELECTOR, "input[data-t='field:input-login']")
    SING_IN_BTN = (By.CSS_SELECTOR, "button[data-t='button:action:passp:sign-in']")
    PASSWORD_FIELD = (By.CSS_SELECTOR, "input[data-t='field:input-passwd']")
    AVATAR_BTN = (By.XPATH, "//span[@class=\"avatar__image-wrapper\"]")
    USER_MENU_FRAME = (By.XPATH, "//iframe[@class='usermenu-portal__iframe']")
    DISK_BTN = (By.XPATH, "//div[@class='List Menu']/a[4]")
    CLOSE_ALERT_BUTTON = (By.CSS_SELECTOR, "button[class='simple-popup__close']")


class DiskPageLocators:
    CREATE_BTN = (By.XPATH, "//span[@class='create-resource-popup-with-anchor']")
    CREATE_FOLDER_BTN = (By.XPATH, "//div[@class='create-resource-popup-with-anchor__create-items']/button[1]")
    CREATE_TEXT_DOC_BTN = (By.XPATH, "//div[@class='create-resource-popup-with-anchor__create-items']/button[2]")
    INPUT_NAME_FIELD = (By.CSS_SELECTOR, "div.dialog__body input")
    CREATE_SUBMIT_BTN = (By.CSS_SELECTOR, "div.dialog__body button")
    ALL_FILES_NAME = (By.CSS_SELECTOR, "div[class='listing-item__title listing-item__title_overflow_clamp']")
    AVATAR_BTN = (By.CSS_SELECTOR, "div[class='PSHeader-User PSHeader-User_noUserName promozavr-anchor-user']")
    LOGOUT_BTN = (By.XPATH, "//ul[@class='menu__group']/li[6]")
    UPLOAD_BTN = (By.CSS_SELECTOR, "input[class='context-menu-create-popup__upload-input']")
    CONTEXT_FIELD = (By.CSS_SELECTOR, "div[class='root__content-container']")

    @staticmethod
    def docx_file(name: str):
        return (By.CSS_SELECTOR, f"div.listing-item__info div[aria-label='{name}.docx']")

    @staticmethod
    def folder(name:str):
        return (By.CSS_SELECTOR, f"div.listing-item__info div[aria-label='{name}']")
