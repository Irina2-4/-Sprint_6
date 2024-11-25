import pytest
from pages.main_page import MainPage
from conftest import driver
from helpers.data import Question
import allure


class TestMainPage:
    @allure.title('Проверка правильности отображения выпадающего списка в разделе "Вопросы о важном"')
    @pytest.mark.parametrize('num,result', Question.answer)

    def test_question_and_answers(self,driver,num,result):
        main_page = MainPage(driver)
        main_page.click_cookies()
        assert main_page.get_answer_text(num) == result
