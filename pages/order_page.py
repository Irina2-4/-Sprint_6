from pages.base_page import BasePage
from locators.order_page_locators import OrderLocators
from helpers import generator
import allure

class OrderPages(BasePage):
    @allure.step('Клик на кнопку "Заказать" вверху страницы')
    def click_order_button_at_the_top_of_the_screen(self):
        self.click_to_element(OrderLocators.BUTTON_ORDER_TOP)

    @allure.step('Клик на кнопку "Заказать" посередине страницы')
    def click_order_button_in_the_middle_of_the_screen(self):
        self.click_to_element(OrderLocators.BUTTON_ORDER_MIDDLE)

    @allure.step('Ввод имени пользователя')
    def set_order_name(self):
        name = generator.generate_name()
        self.add_text_to_element(OrderLocators.NAME,name)

    @allure.step('Ввод фамилии пользователя')
    def set_order_last_name(self):
        last_name = generator.generate_last_name()
        self.add_text_to_element(OrderLocators.LAST_NAME,last_name)

    @allure.step('Ввод адреса пользователя')
    def set_order_address(self):
        address = generator.generate_address()
        self.add_text_to_element(OrderLocators.ADDRESS, address)

    @allure.step('Ввод ближайшей станции метро')
    def set_order_metro(self):
        metro = generator.generate_metro()
        self.click_to_element(OrderLocators.METRO)
        locator = self.format_locator(OrderLocators.METRO_DROP_DOWN_LIST,metro)
        self.click_to_element(locator)

    @allure.step('Ввод телефона пользователя')
    def set_order_phone(self):
        phone = generator.generate_phone()
        self.add_text_to_element(OrderLocators.PHONE,phone)

    @allure.step('Клик на кнопку "Далее"')
    def click_button_continue(self):
        self.click_to_element(OrderLocators.NEXT)

    @allure.step('Ввод даты доставки')
    def set_order_date(self):
        rent_date = generator.generate_rent_date()
        self.add_text_to_element(OrderLocators.DATE,rent_date)
        self.click_to_element(OrderLocators.ABOUT)

    @allure.step('Ввод срока аренды самоката')
    def set_order_rental_period(self):
        rental_period = generator.generate_days()
        self.click_to_element(OrderLocators.RENT_PERIOD)
        locator = self.format_locator(OrderLocators.RENT_PERIOD_DROP_DOWN_LIST,rental_period)
        self.click_to_element(locator)

    @allure.step('Ввод цвета самоката')
    def set_order_color(self):
        color = generator.generate_color()
        locator = self.format_locator(OrderLocators.COLOR,color)
        self.click_to_element(locator)

    @allure.step('Добавление комментария')
    def set_order_comment(self):
        comment = generator.generate_comment()
        self.add_text_to_element(OrderLocators.COMMENT,comment)

    @allure.step('Клик на кнопку "Заказать"')
    def set_order_click_order(self):
        self.click_to_element(OrderLocators.ORDER_B)

    @allure.step('Подтверждение заказа')
    def set_order_click_yes(self):
        self.click_to_element(OrderLocators.BUTTON_YES)

    @allure.step('Проверка успешности заказа')
    def check_order(self):
        return self.find_element_with_wait(OrderLocators.BUTTON_STATUS).is_displayed()

    @allure.step('Проверка статуса заказа')
    def set_status(self):
        return self.get_text_from_element(OrderLocators.STATUS_BUTTON)
