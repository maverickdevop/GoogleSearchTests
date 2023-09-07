""" Локаторы для сех страниц
    В теством молько для страницы логина и авторизации """

from selenium.webdriver.common.by import By


class GooglePage:
    GOOGLE_LOGO = (By.XPATH, "//img[@alt='Google']")
    SEARCH_INPUT = (By.NAME, "q")
    SCREEN_KEYBOARD = (By.XPATH, "//div[@aria-label='Экранная клавиатура']/span")

    BUTTONS = {
        'P': (By.XPATH, "//button[@id='K71']"),
        'Y': (By.XPATH, "//button[@id='K66']"),
        'T': (By.XPATH, "//button[@id='K78']"),
        'O': (By.XPATH, "//button[@id='K74']"),
        'N': (By.XPATH, "//button[@id='K89']"),
    }

    SEARCH_BTN = (By.XPATH, "//input[@type='submit' and @role='button']")
    SUGGEST_LIST = (By.XPATH, "(//ul[@role='listbox']//span[normalize-space()])[position() mod 2 = 1]")
    RESULT = (By.XPATH, "//h3[normalize-space()='Welcome to Python.org']")
    SEARCH_BY_IMG = (By.XPATH, "//div[@aria-label='Поиск по картинке']")
    IMG_DROPZONE = (By.XPATH, "//span[@role='button']")