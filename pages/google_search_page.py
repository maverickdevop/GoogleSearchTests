from pages.base_methods import BasePage
from pages.locators import GooglePage
from configs.data import DataParameters as Data
from configs.enums import GlobalErrorMessages
import time
import os


class GoogleSearchPage(BasePage):
    """ Методы для создания тестов """

    def input_word_and_check_in_search_list(self):
        """ Метод проверки поиска по названию в Google """
        self.send_keys(GooglePage.SEARCH_INPUT, Data.KEYWORD)
        self.assert_text_in_list(GooglePage.SUGGEST_LIST, Data.KEYWORD), GlobalErrorMessages.WRONG_TEXT.value
        self.do_click(GooglePage.SEARCH_BTN)
        self.assert_query_parameter_in_url(Data.KEYWORD), GlobalErrorMessages.WRONG_URL.value
        self.check_element(GooglePage.RESULT), GlobalErrorMessages.WRONG_TEXT.value

    def input_word_with_keyboard_and_check_in_search_list(self, button_names):
        """ Метод проверки поиска по названию в Google
            1. Активировать экранную клавиатуру
            2. Ввести текст
            3. Проверить текст в предложенном списке и странице с результатами"""
        self.do_click(GooglePage.SCREEN_KEYBOARD)
        self.do_click_keyboard(button_names)
        time.sleep(1)
        self.assert_word_in_list(GooglePage.SUGGEST_LIST, Data.KEYWORD_RU), GlobalErrorMessages.WRONG_TEXT.value
        self.do_click(GooglePage.SEARCH_BTN)
        time.sleep(0.5)
        self.check_element(GooglePage.RESULT), GlobalErrorMessages.WRONG_TEXT.value

    def should_be_search_by_image(self):
        """ Метод проверки кнопки поиска по картинке в Google """
        self.check_element(GooglePage.SEARCH_BY_IMG), GlobalErrorMessages.WRONG_ELEMENT.value

    def search_by_image(self):
        """ Метод проверки поиска по картинке в Google
            1. Загрузить картинку
            2. Проверить, что Lens сработал"""
        self.should_be_search_by_image()
        self.do_click(GooglePage.SEARCH_BY_IMG)
        time.sleep(1)
        self.upload_data(GooglePage.IMG_DROPZONE)
