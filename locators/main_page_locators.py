from selenium.webdriver.common.by import By

class MainPageLoc:

    # Локатор вопросов
    QUESTION_LOCATOR = By.XPATH, '//div[@id = "accordion__heading-{}"]'
    #Локатор ответов
    ANSWER_LOCATOR = By.XPATH, '//div[@id = "accordion__panel-{}"]'
    #Локатор последнего вопроса
    QUESTION_LOCATOR_LAST = By.XPATH, '//div[@id = "accordion__heading-7"]'
    #Локатор кнопки "Яндекс"
    YANDEX_LOCATOR = By.XPATH, '//*[@href = "//yandex.ru"]'
    #Локатор кук
    COOKIES_LOCATOR = By.ID, 'rcc-confirm-button'
    #Локатор кнопки "Самокат"
    SAMOKAT_LOCATOR = By.XPATH, '//*[contains(@class, "Header_LogoScooter")]'
    # Локатор кнопки"Найти" в Яндекс-Дзене
    DZEN_PAGE_LOCATOR = By.XPATH, '//*[text() = "Найти"]'