from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import string
import random
from test_login import login_user
from test_login import login_check
from data import *


def generate_credentials(name_length, email_length, password_length):
    if name_length < 1 or name_length > 100 or email_length < 1 or email_length > 100 or password_length < 1 or password_length > 100:
        raise ValueError("Допустимая длина от 1 до 100")
    else:
        characters = string.ascii_letters + string.digits
        name = ''.join(random.choice(characters) for i in range(name_length))
        email = f'{"".join(random.choice(characters) for i in range(email_length))}@ya.ru'
        password = ''.join(random.choice(characters)
                           for i in range(password_length))
        return (name, email, password)


def register(driver, name, email, password):
    driver.get(reg_page)
    WebDriverWait(driver, 2).until(expected_conditions.element_to_be_clickable(
        (By.XPATH, reg_button)))
    driver.find_element(By.XPATH, name_field).send_keys(name)
    driver.find_element(By.XPATH, email_field).send_keys(email)
    driver.find_element(By.XPATH, password_field).send_keys(password)
    driver.find_element(By.XPATH, reg_button).click()


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
