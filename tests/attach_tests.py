# coding=utf-8
from components.login_and_write import login_and_write

from pages.file_attaching_page import FileAttachingPage
from tests.base_test import BaseTest


class AttachTests(BaseTest):
    # ATTACH_FILE_BUTTON =

    TEST_FILE_XLSX = './test_files/АДАМОВА!.xlsx'

    def test(self):
        login_and_write(self.driver, self.USEREMAIL, self.PASSWORD)
        # форматирование письма
        file_attaching_page = FileAttachingPage(self.driver)
        file_attaching_form = file_attaching_page.form
        file_attaching_form.open_writing_letter()
        file_attaching_form.set_file_attach_input()
        file_attaching_form.send_keys_to_input(self.TEST_FILE_XLSX)
        file_attaching_form.set_destionation_email()
        file_attaching_form.click_send_button()

        self.assertEqual(file_attaching_form.checkMessageSent(), True)
