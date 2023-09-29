from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from test_login import login_user
from data import *


def open_account(driver):
    WebDriverWait(driver, 2).until(expected_conditions.element_to_be_clickable(
        (By.XPATH, account_button))).click()
    WebDriverWait(driver, 2).until(
        expected_conditions.element_to_be_clickable((By.XPATH, save_button)))


def test_open_account(driver):
    driver.get(login_page)
    login_user(driver, valid_email, valid_password)
    open_account(driver)
    for text in texts_on_account_page:
        assert text in driver.page_source
