import pytest
from locators.constructor_page_locators import ConstructorPageLocators
from urls import BASE_URL

tabs = [
    (ConstructorPageLocators.BUNS_TAB, ConstructorPageLocators.BUNS_TAB_ACTIVE),
    (ConstructorPageLocators.SAUCES_TAB, ConstructorPageLocators.SAUCES_TAB_ACTIVE),
    (ConstructorPageLocators.FILLINGS_TAB, ConstructorPageLocators.FILLINGS_TAB_ACTIVE),
]

class TestConstructorTabs:

    @pytest.mark.parametrize("tab_locator,active_locator", tabs)
    def test_tab(self, driver, tab_locator, active_locator):
        driver.get(BASE_URL)
        driver.find_element(*tab_locator).click()
        assert driver.find_element(*active_locator).is_displayed()
