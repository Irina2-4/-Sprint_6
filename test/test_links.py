from pages.order_page import OrderPages
from pages.main_page import MainPage
from conftest import driver
from helpers.data import Urls
import allure


@allure.title('Тестирование перехода по ссылкам на главную страницу "Самоката" и на страницу "Дзен"')
class TestLinks:
    def test_click_yandex(self,driver):
        main_page = MainPage(driver)
        main_page.click_cookies()
        main_page.check_link_yandex()
        assert driver.current_url == Urls.DZEN_URL

    def test_click_scooter(self,driver):
        main_page = MainPage(driver)
        order_page = OrderPages(driver)
        main_page.click_cookies()
        order_page.click_order_button_at_the_top_of_the_screen()
        main_page.check_link_scooter()
        assert driver.current_url == Urls.MAIN_URL

