import pytest
from locators.personal_account_locators import PersonalAccountLocators
from urls import LOGIN_URL, BASE_URL
from data import EXISTING_USER_EMAIL, EXISTING_USER_PASSWORD

class TestPersonalAccount:

    def test_redirect_to_personal_account(self, driver):
        driver.get(LOGIN_URL)
        driver.find_element(*PersonalAccountLocators.EMAIL_INPUT).send_keys(EXISTING_USER_EMAIL)
        driver.find_element(*PersonalAccountLocators.PASSWORD_INPUT).send_keys(EXISTING_USER_PASSWORD)
        driver.find_element(*PersonalAccountLocators.LOGIN_BUTTON).click()
        driver.find_element(*PersonalAccountLocators.PERSONAL_ACCOUNT_BUTTON).click()
        assert "account" in driver.current_url

    def test_logout_from_personal_account(self, driver):
        driver.get(LOGIN_URL)
        driver.find_element(*PersonalAccountLocators.EMAIL_INPUT).send_keys(EXISTING_USER_EMAIL)
        driver.find_element(*PersonalAccountLocators.PASSWORD_INPUT).send_keys(EXISTING_USER_PASSWORD)
        driver.find_element(*PersonalAccountLocators.LOGIN_BUTTON).click()
        driver.find_element(*PersonalAccountLocators.LOGOUT_BUTTON).click()
        assert "login" in driver.current_url