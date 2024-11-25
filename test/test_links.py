from pages.order_page import OrderPages
from pages.main_page import MainPage
from conftest import driver
from helpers.Urls import Urls
import allure



class TestLinks:
    @allure.title('Тестирование перехода по ссылкам на страницу "Дзен"')
    def test_click_yandex(self,driver):
        main_page = MainPage(driver)
        main_page.click_cookies()
        main_page.check_link_yandex()
        assert driver.current_url == Urls.DZEN_URL


    @allure.title('Тестирование перехода по ссылкам на главную страницу "Самоката"')
    def test_click_scooter(self,driver):
        main_page = MainPage(driver)
        order_page = OrderPages(driver)
        main_page.click_cookies()
        order_page.click_order_button_at_the_top_of_the_screen()
        main_page.check_link_scooter()
        assert driver.current_url == Urls.MAIN_URL

