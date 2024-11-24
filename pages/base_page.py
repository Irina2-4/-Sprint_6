from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import allure
@allure.title('Набор базовых методов')
class BasePage:

    @allure.step('Загрузка драйвера')
    def __init__(self,driver):
        self.driver = driver

    @allure.step('Поиск элемента на странице')
    def find_element_with_wait(self,locator):
        WebDriverWait(self.driver,3).until(expected_conditions.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    @allure.step('Клик на элемент')
    def click_to_element(self,locator):
        WebDriverWait(self.driver,5).until(expected_conditions.element_to_be_clickable(locator))
        self.driver.find_element(*locator).click()

    @allure.step('Добавление текста на элемент')
    def add_text_to_element(self,locator,text):
        self.find_element_with_wait(locator).send_keys(text)

    @allure.step('Текст элементa')
    def get_text_from_element(self,locator):
       return self.find_element_with_wait(locator).text

    @allure.step('Скролл страницы')
    def scroll_to_element(self,locator):
        element = self.find_element_with_wait(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step('Принятие кук')
    def get_cookies(self,locator):
        WebDriverWait(self.driver,3).until(expected_conditions.visibility_of_element_located(locator)).click()

    @allure.step('Формат локатора')

    def format_locator(self,locator_1,num):
        method,locator = locator_1
        locator = locator.format(num)
        return method, locator