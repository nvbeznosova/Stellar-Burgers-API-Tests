import pytest
from locators.registration_page_locators import RegistrationPageLocators
from urls import REGISTRATION_URL
from utils import generate_email, generate_password

class TestRegistration:

    def test_successful_registration(self, driver):
        email = generate_email()
        password = generate_password()

        driver.get(REGISTRATION_URL)
        driver.find_element(*RegistrationPageLocators.NAME_INPUT).send_keys("Nadia Beznosova")
        driver.find_element(*RegistrationPageLocators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*RegistrationPageLocators.PASSWORD_INPUT).send_keys(password)
        driver.find_element(*RegistrationPageLocators.REGISTER_BUTTON).click()
        assert "login" in driver.current_url

    def test_invalid_password_registration(self, driver):
        email = generate_email()

        driver.get(REGISTRATION_URL)
        driver.find_element(*RegistrationPageLocators.NAME_INPUT).send_keys("Nadia Beznosova")
        driver.find_element(*RegistrationPageLocators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*RegistrationPageLocators.PASSWORD_INPUT).send_keys("123")
        driver.find_element(*RegistrationPageLocators.REGISTER_BUTTON).click()
        assert driver.find_element(*RegistrationPageLocators.ERROR_MESSAGE).is_displayed()
