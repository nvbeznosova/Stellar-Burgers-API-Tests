from selenium.webdriver.common.by import By

class ConstructorPageLocators:
    BUNS_TAB = (By.XPATH, "//span[text()='Булки']")
    BUNS_TAB_ACTIVE = (By.XPATH, "//div[@class='tab_tab__2BEPc tab_tab_type_current__1SBnE']/span[text()='Булки']")

    SAUCES_TAB = (By.XPATH, "//span[text()='Соусы']")
    SAUCES_TAB_ACTIVE = (By.XPATH, "//div[@class='tab_tab__2BEPc tab_tab_type_current__1SBnE']/span[text()='Соусы']")

    FILLINGS_TAB = (By.XPATH, "//span[text()='Начинки']")
    FILLINGS_TAB_ACTIVE = (By.XPATH, "//div[@class='tab_tab__2BEPc tab_tab_type_current__1SBnE']/span[text()='Начинки']")
