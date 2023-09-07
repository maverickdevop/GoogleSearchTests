from tests.base_test import BaseTest
from pages.google_main_page import GoogleMainPage
from configs.data import DataParameters as Data
import allure


@allure.severity(allure.severity_level.CRITICAL)
@allure.suite('Тесты на проверку коррекной работы главной страницы поисковика Google.com')
class TestGooglePage(BaseTest):

    def setup(self):
        self.google = GoogleMainPage(self.driver)
        self.google.open_page(Data.URL)

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.testcase('Проверка, что мы попадаем на страницу Google')
    def test_should_be_google_search_page(self):
        self.google.should_be_google_search_page()

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.testcase('Проверка, что форма поиска на странице отображается корректно')
    def test_should_be_correct_login_form(self):
        self.google.should_be_correct_login_form()