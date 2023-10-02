from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from data import *
from utils import *


def test_registration_valid_credentials(driver):
    name, email, password = generate_credentials(4, 10, 6)
    register(driver, name, email, password)
    login_user(driver, email, password)
    login_check(driver)


def test_registration_with_too_short_password(driver):
    name, email, password = generate_credentials(4, 10, 5)
    register(driver, name, email, password)
    assert 'Некорректный пароль' in driver.find_element(
        By.CLASS_NAME, "input__error").text
