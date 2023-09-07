from tests.base_test import BaseTest
from pages.google_search_page import GoogleSearchPage
from configs.data import DataParameters as Data
from pages.locators import GooglePage
import allure


@allure.severity(allure.severity_level.CRITICAL)
@allure.suite('Тесты на проверку коррекной работы поиска по запросу в Google.com')
class TestGoogleSearchPage(BaseTest):

    def setup(self):
        self.search = GoogleSearchPage(self.driver)
        self.search.open_page(Data.URL)

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.testcase('Проверка, что поиск по фразе в Google работает корректно')
    def test_search_by_keyword_name_in_google(self):
        self.search.input_word_and_check_in_search_list()

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.testcase('Проверка, что поиск с виртуальной клавиатурой в Google работает')
    def test_search_by_virtual_keyword_in_google(self):
        button_names = ['P', 'Y', 'T', 'O', 'N']
        self.search.input_word_with_keyboard_and_check_in_search_list(button_names)

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.testcase('Проверка, что поиск по картинке в Google работает')
    def test_search_by_image_in_google(self):
        self.search.search_by_image()
