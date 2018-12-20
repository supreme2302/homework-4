# coding=utf-8
import os
import unittest
from components.login_and_write import login_and_write
from pages.letter_formatting_page import LetterFormattingPage
from tests.base_test import BaseTest


class LetterFormattingTests(BaseTest):
    SAMPLE_TEXT = 'hello'
    NOT_BOLD_TEXT = '</strong>​​​​​​​' + SAMPLE_TEXT
    BOLD_TEXT = '<strong>​​​​​​​' + SAMPLE_TEXT + '</strong>'
    ITALIC_TEXT = '<em>​​​​​​​' + SAMPLE_TEXT + '</em>'
    UNDERLINED_TEXT = '<u>​​​​​​​' + SAMPLE_TEXT + '</u>'
    STRIKETHROUGH_TEXT = '<s>​​​​​​​' + SAMPLE_TEXT + '</s>'
    TEXT_COLOR = 'rgba(202, 242, 245, 1)'
    FONT_SIZE = '32px'
    LINE_HEIGHT = '40px'
    TEXT_ALIGN = 'right'
    MARGIN_LEFT = '40px'
    LISTED_TEXT = '<li>​​​​​​​' + SAMPLE_TEXT + '</li>'
    EMPTY_FIELD = '<br>'
    LINK = 'https://vk.com/'

    def test(self):
        login_and_write(self.driver, self.USEREMAIL, self.PASSWORD)




        letter_formatting_form.click_cancel_writing_message()
        letter_formatting_form.open_writing_letter()

        # очистка поля ввода сообещния
        letter_formatting_form.clear_field()

        # проверка списка
        # нумерованный список
        letter_formatting_form.click_on_list_icon()
        letter_formatting_form.click_on_numbered_list()
        # letter_formatting_form.click_on_message_field()
        letter_formatting_form.write_some_text(self.SAMPLE_TEXT)
        numberred_list = letter_formatting_form.get_numbered_text()
        self.assertEqual(self.LISTED_TEXT.decode('utf-8'), numberred_list)

        letter_formatting_form.click_cancel_writing_message()
        letter_formatting_form.open_writing_letter()

        # очистка поля ввода сообещния
        letter_formatting_form.clear_field()

        # маркированный список
        letter_formatting_form.click_on_list_icon()
        letter_formatting_form.click_on_bulleted_list()
        letter_formatting_form.write_some_text(self.SAMPLE_TEXT)
        bulleted_list = letter_formatting_form.get_bulleted_text()
        self.assertEqual(self.LISTED_TEXT.decode('utf-8'), bulleted_list)

        # проверка работы кнопки отменить
        letter_formatting_form.click_on_cancel_icon()
        self.assertEqual(self.LISTED_TEXT.decode('utf-8'), numberred_list)
        letter_formatting_form.click_on_cancel_icon()
        letter_formatting_form.click_on_cancel_icon()
        empty_field = letter_formatting_form.get_text()
        self.assertEqual(self.EMPTY_FIELD, empty_field)

        # проверка работы кнопки отменить
        letter_formatting_form.click_on_repeat_icon()
        letter_formatting_form.click_on_repeat_icon()
        self.assertEqual(self.LISTED_TEXT.decode('utf-8'), numberred_list)

        # очистка поля ввода сообещния
        letter_formatting_form.click_on_cancel_icon()
        letter_formatting_form.click_on_cancel_icon()

        # проверка вствки ссылки
        letter_formatting_form.click_on_link_icon()
        letter_formatting_form.write_some_text(self.LINK)
        letter_formatting_form.click_on_tab_key()
        letter_formatting_form.write_some_text(self.SAMPLE_TEXT)
        letter_formatting_form.click_on_ok_link_button()
        href, linked_text = letter_formatting_form.get_link()
        self.assertEqual(self.SAMPLE_TEXT, linked_text)
        self.assertEqual(self.LINK.decode('utf-8'), href)

        # очистка поля ввода сообещния
        letter_formatting_form.clear_field()

        # проверка вставки картинки
        letter_formatting_form.send_picture()
        img = letter_formatting_form.get_img()
        self.assertIn('<img', img)

        # очистка поля ввода сообещния
        letter_formatting_form.click_cancel_writing_message()
        letter_formatting_form.open_writing_letter()

        # очистка поля ввода сообещния
        letter_formatting_form.clear_field()

        # проверка очистки форматирования
        letter_formatting_form.click_on_bold_icon()
        letter_formatting_form.click_on_clear_formatting_icon()
        letter_formatting_form.click_on_message_field()
        letter_formatting_form.write_some_text(self.SAMPLE_TEXT)
        text = letter_formatting_form.get_text()
        self.assertIn(self.NOT_BOLD_TEXT.decode('utf-8'), text)
