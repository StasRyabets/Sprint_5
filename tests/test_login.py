from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from data import *


def login_user(driver, email, password):
    WebDriverWait(driver, 2).until(
        expected_conditions.element_to_be_clickable((By.XPATH, login_button)))
    driver.find_element(By.XPATH, email_field).send_keys(email)
    driver.find_element(By.XPATH, password_field).send_keys(password)
    driver.find_element(By.XPATH, login_button).click()


def login_check(driver):
    assert WebDriverWait(driver, 2).until(expected_conditions.visibility_of_element_located(
        (By.XPATH, order_button))) is not None


def test_login_from_home_page(driver):
    driver.get(home_page)
    WebDriverWait(driver, 2).until(expected_conditions.element_to_be_clickable(
        (By.XPATH, login_from_home_page_button))).click()
    login_user(driver, valid_email, valid_password)
    login_check(driver)


def test_login_from_account_page(driver):
    driver.get(account_page)
    login_user(driver, valid_email, valid_password)
    login_check(driver)


def test_login_from_registration_page(driver):
    driver.get(reg_page)
    WebDriverWait(driver, 2).until(expected_conditions.element_to_be_clickable(
        (By.XPATH, login_from_reg_page_button))).click()
    login_user(driver, valid_email, valid_password)
    login_check(driver)


def test_login_from_password_recovery_page(driver):
    driver.get(password_recovery_page)
    WebDriverWait(driver, 2).until(expected_conditions.element_to_be_clickable(
        (By.XPATH, login_from_reg_page_button))).click()
    login_user(driver, valid_email, valid_password)
    login_check(driver)
