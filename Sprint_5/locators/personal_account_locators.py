from selenium.webdriver.common.by import By

class PersonalAccountLocators:
    EMAIL_INPUT = (By.NAME, "email")
    PASSWORD_INPUT = (By.NAME, "password")
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, "//p[text()='Личный кабинет']")
    LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выйти']")
    CONSTRUCTOR_LINK = (By.XPATH, "//p[text()='Конструктор']")
    LOGO_LINK = (By.XPATH, "//div[@class='AppHeader_header__logo__2D0X2']")
