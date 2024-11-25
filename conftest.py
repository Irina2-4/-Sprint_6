import pytest
from selenium import webdriver
from helpers.Urls import Urls

@pytest.fixture(scope = 'function')
def driver():
# инициализируем драйвер браузера
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get(Urls.MAIN_URL)
    yield driver
# закроем браузер
    driver.quit()
