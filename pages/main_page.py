from locators.main_page_locators import MainPageLoc
from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import allure

class MainPage(BasePage):
    @allure.step('Получение ответа')
    def get_answer_text(self,num):
        locator_q_formatted = self.format_locator(MainPageLoc.QUESTION_LOCATOR,num)
        locator_a_formatted = self.format_locator(MainPageLoc.ANSWER_LOCATOR,num)
        self.scroll_to_element(MainPageLoc.QUESTION_LOCATOR_LAST)
        self.click_to_element(locator_q_formatted)
        return self.get_text_from_element(locator_a_formatted)
    @allure.step('Клик на вопрос')
    def click_answer_and_question(self,num):
        method,locator = MainPageLoc.QUESTION_LOCATOR
        locator = locator.format(num)
        WebDriverWait(self.driver,3).until(expected_conditions.visibility_of_element_located((method,locator)))
        return self.click_to_element((method,locator))

    @allure.step('Клик на логотип Яндекс')
    def click_yandex(self):
        self.click_to_element(MainPageLoc.YANDEX_LOCATOR)


    @allure.step('Клик на логотип "Самоката"')
    def click_scooter(self):
        self.click_to_element(MainPageLoc.SAMOKAT_LOCATOR)

    @allure.step('Проверка пререхода на Дзен')
    def check_link_yandex(self):
        self.click_yandex()
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.find_element_with_wait(MainPageLoc.DZEN_PAGE_LOCATOR)

    @allure.step('Проверка пререхода на главную страницу "Самоката"')
    def check_link_scooter(self):
        self.click_scooter()
        self.find_element_with_wait(MainPageLoc.SAMOKAT_LOCATOR)

    @allure.step('Принимаем куки')
    def click_cookies(self):
        self.get_cookies(MainPageLoc.COOKIES_LOCATOR)