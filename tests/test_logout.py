from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from test_login import login_user
from tests.test_account import open_account

email = "stasriabets1042@ya.uz"
password = "123456"


def test_logout_from_account(driver):
    driver.get("https://stellarburgers.nomoreparties.site/login")
    login_user(driver, email, password)
    open_account(driver)
    WebDriverWait(driver, 2).until(expected_conditions.element_to_be_clickable(
        (By.XPATH, "//button[text()='Выход']"))).click()
    assert WebDriverWait(driver, 2).until(expected_conditions.element_to_be_clickable(
        (By.XPATH, "//button[text()='Войти']"))) is not None
