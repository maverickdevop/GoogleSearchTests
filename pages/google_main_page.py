from pages.base_methods import BasePage
from pages.locators import GooglePage
from configs.data import DataParameters as Data
from configs.enums import GlobalErrorMessages

class GoogleMainPage(BasePage):
    """ Методы для создания тестов """

    def should_be_google_search_page(self):
        """ Метод проверки корректного окна логина и title """
        assert self.check_element(GooglePage.GOOGLE_LOGO), GlobalErrorMessages.WRONG_ELEMENT.value
        assert self.get_page_title() == Data.GOOGLE_TITLE, GlobalErrorMessages.WRONG_TITLE.value

    def should_be_search_input(self):
        """ Метод проверки наличия инпута по названию """
        assert self.check_element(GooglePage.SEARCH_INPUT), GlobalErrorMessages.WRONG_ELEMENT.value

    def should_be_search_button(self):
        """ Метод проверки наличия кнопки поиска """
        assert self.check_element(GooglePage.SEARCH_BTN), GlobalErrorMessages.WRONG_ELEMENT.value

    def should_be_correct_login_form(self):
        """ Объединение методов поиска элементов """
        self.should_be_search_input()
        self.should_be_search_button()

    def input_word_and_check_in_search_list(self):
        """ Метод проверки поиска по названию в Google """
        self.send_keys(GooglePage.SEARCH_INPUT, Data.KEYWORD)
        self.assert_text_in_list(GooglePage.SUGGEST_LIST, "innerText", Data.KEYWORD)
        self.do_click(GooglePage.SEARCH_BTN)
        self.assert_query_parameter_in_url(Data.KEYWORD)