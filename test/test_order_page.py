from conftest import driver
from pages.main_page import MainPage
from pages.order_page import OrderPages
import allure


class TestOrderPage:
    @allure.title('Проверка заказа самоката при нажатии на кнопку "Заказать" сверху страницы')
    def test_order_button_at_the_top_of_the_screen(self,driver):
        main_page = MainPage(driver)
        order_page = OrderPages(driver)
        main_page.click_cookies()
        order_page.click_order_button_at_the_top_of_the_screen()
        order_page.set_order_name()
        order_page.set_order_last_name()
        order_page.set_order_address()
        order_page.set_order_metro()
        order_page.set_order_phone()
        order_page.click_button_continue()
        order_page.set_order_date()
        order_page.set_order_rental_period()
        order_page.set_order_color()
        order_page.set_order_comment()
        order_page.set_order_click_order()
        order_page.set_order_click_yes()
        assert order_page.set_status() =='Посмотреть статус'

    @allure.title('Проверка заказа самоката при нажатии на кнопку "Заказать в середине страницы"')
    def test_order_button_in_the_middle_of_the_screen(self,driver):
        main_page = MainPage(driver)
        order_page = OrderPages(driver)
        main_page.click_cookies()
        order_page.click_order_button_in_the_middle_of_the_screen()
        order_page.set_order_name()
        order_page.set_order_last_name()
        order_page.set_order_address()
        order_page.set_order_metro()
        order_page.set_order_phone()
        order_page.click_button_continue()
        order_page.set_order_date()
        order_page.set_order_rental_period()
        order_page.set_order_color()
        order_page.set_order_comment()
        order_page.set_order_click_order()
        order_page.set_order_click_yes()
        assert order_page.set_status() =='Посмотреть статус'