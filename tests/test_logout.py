from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from data import *
from utils import *


def test_logout_from_account(driver):
    driver.get(login_page)
    login_user(driver, valid_email, valid_password)
    open_account(driver)
    WebDriverWait(driver, 2).until(expected_conditions.element_to_be_clickable(
        (By.XPATH, logout_button))).click()
    assert WebDriverWait(driver, 2).until(expected_conditions.element_to_be_clickable(
        (By.XPATH, login_button))) is not None
