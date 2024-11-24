from selenium.webdriver.common.by import By

class OrderLocators:
    #Локаторы главной страницы

    # кнопка "Заказать" вверху экрана
    BUTTON_ORDER_TOP =By.XPATH, "//div[contains(@class, 'Header_Nav')]/button[text()='Заказать']"
    # кнопка "Статус заказа"
    BUTTON_STATUS = By.XPATH, "//a[text() = 'Статус заказа']"
    # кнопка "Заказать" в середине экрана
    BUTTON_ORDER_MIDDLE = By.XPATH, "//div[contains(@class, 'Home_FinishButton')]/button[text()='Заказать']"

    #Локаторы заказа

    # поле для ввода имени
    NAME = By.XPATH,"//input[@placeholder = '* Имя']"
    # поле ввода фамилии
    LAST_NAME = By.XPATH,"//input[@placeholder = '* Фамилия']"
    #поле ввода адреса
    ADDRESS = By.XPATH,"//input[@placeholder = '* Адрес: куда привезти заказ']"
    # поле ввода телефона
    PHONE = By.CSS_SELECTOR, "input[placeholder='* Телефон: на него позвонит курьер']"
    # поле ввода даты заказа
    DATE = By.XPATH,".//input[@placeholder = '* Когда привезти самокат']"
    # выбор цвета
    COLOR = By.XPATH, '//*[@id="{}"]'
    #  выбор срока аренды(сутки)
    DAYS_1 = By.XPATH, ".//div[text() = 'сутки']"
    # выбор срока аренды(трое суток)
    DAYS_3 = By.XPATH, ".//div[text() = 'трое суток']"
    #поле выбора станци метро
    METRO = By.XPATH, '//*[@placeholder="* Станция метро"]'
    #локатор списка выбора станции
    METRO_DROP_DOWN_LIST = By.XPATH, '//*[text()="{}"]'
    #кнопка далее
    NEXT = By.XPATH, "//button[text() = 'Далее']"
    #период аренды
    RENT_PERIOD = By.XPATH, ".//span[@class='Dropdown-arrow']"
    #локатор списка периода аренды
    RENT_PERIOD_DROP_DOWN_LIST = By.XPATH, '//*[text()="{}"]'
    #поле ввода комментария для курьера
    COMMENT = By.XPATH, '//*[@placeholder="Комментарий для курьера"]'
    #кнопка "Заказать"
    ORDER_B =  By.XPATH, '//*[contains(@class,"Order_Buttons")]//button[text()="Заказать"]'
    # Кнопка "Да"
    BUTTON_YES = By.XPATH, "//button[text() = 'Да']"
    # Кнопка "Заказ оформлен"
    ORDER_PLACED = By.XPATH, ".//div[text() = 'Заказ оформлен']"
    #Заголовок "Про аренду""
    ABOUT = By.XPATH, '//*[text()="Про аренду"]'
    #Кнопка "Посмотреть статус"
    STATUS_BUTTON = By.XPATH, '//button[contains(@class, "Button_Button") and text() = "Посмотреть статус"]'