import pytest
from locators.login_page_locators import LoginPageLocators
from locators.personal_account_locators import PersonalAccountLocators
from urls import BASE_URL, LOGIN_URL
from data import EXISTING_USER_EMAIL, EXISTING_USER_PASSWORD

class TestLogin:

    def test_login_main_page(self, driver):
        driver.get(BASE_URL)
        driver.find_element(*LoginPageLocators.LOGIN_BUTTON_MAIN).click()
        assert driver.current_url == LOGIN_URL

    def test_login_with_valid_credentials(self, driver):
        driver.get(LOGIN_URL)
        driver.find_element(*LoginPageLocators.EMAIL_FIELD).send_keys(EXISTING_USER_EMAIL)
        driver.find_element(*LoginPageLocators.PASSWORD_FIELD).send_keys(EXISTING_USER_PASSWORD)
        driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
        assert driver.find_element(*PersonalAccountLocators.PERSONAL_ACCOUNT_BUTTON).is_displayed()
