from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

email = "stasriabets1042@ya.uz"
password = "123456"


def login_user(driver, email, password):
    WebDriverWait(driver, 2).until(expected_conditions.element_to_be_clickable(
        (By.XPATH, "//button[text()='Войти']")))
    driver.find_element(
        By.XPATH, "//label[text()='Email']/following-sibling::input[@type='text']"
    ).send_keys(email)
    driver.find_element(
        By.XPATH, "//label[text()='Пароль']/following-sibling::input[@type='password']"
    ).send_keys(password)
    driver.find_element(By.XPATH, "//button[text()='Войти']").click()

    button = WebDriverWait(driver, 2).until(expected_conditions.visibility_of_element_located(
        (By.XPATH, "//button[text()='Оформить заказ']")))
    assert button.text == "Оформить заказ"


def test_login_from_home_page(driver):
    driver.get("https://stellarburgers.nomoreparties.site")
    WebDriverWait(driver, 2).until(expected_conditions.element_to_be_clickable(
        (By.XPATH, "//button[text()='Войти в аккаунт']"))).click()
    login_user(driver, email, password)


def test_login_from_account_page(driver):
    driver.get("https://stellarburgers.nomoreparties.site/account")
    login_user(driver, email, password)


def test_login_from_registration_page(driver):
    driver.get("https://stellarburgers.nomoreparties.site/register")
    WebDriverWait(driver, 2).until(expected_conditions.element_to_be_clickable(
        (By.XPATH, '//a[@href="/login"]'))).click()
    login_user(driver, email, password)


def test_login_from_password_recovery_page(driver):
    driver.get("https://stellarburgers.nomoreparties.site/forgot-password")
    WebDriverWait(driver, 2).until(expected_conditions.element_to_be_clickable(
        (By.XPATH, '//a[@href="/login"]'))).click()
    login_user(driver, email, password)
