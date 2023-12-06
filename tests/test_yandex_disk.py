from ..pages.auth_page import AuthPage
from ..pages.disk_page import DiskPage
from ..data.verification_data import VerData


def test_create_file(browser, logout):
    auth_page = AuthPage(browser)
    disk_page = DiskPage(browser)

    auth_page.login()
    auth_page.open_disk_page()
    disk_page.create_folder("TestFolder")
    disk_page.open_by_double_click("TestFolder")
    disk_page.create_docs_file(VerData.DOCX_FILE_NAME)

    assert disk_page.check_file_is_created(VerData.DOCX_FILE_NAME), f"Элемент {VerData.DOCX_FILE_NAME} не создан"
    assert disk_page.check_file_name(VerData.DOCX_FILE_NAME) == "TestName.docx"


"""Задание со звездочкой, готовое на 70%"""
def test_upload_txt_file(browser):
    auth_page = AuthPage(browser)
    disk_page = DiskPage(browser)

    auth_page.login()
    auth_page.open_disk_page()
    disk_page.create_folder("TestFolder")
    disk_page.open_by_double_click("TestFolder")
    disk_page.upload_file("TestTxtFile.txt")
    disk_page.open_by_double_click("TestTxtFile.txt")
    disk_page.open("TestName")
