from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from test_login import login_user

email = "stasriabets1042@ya.uz"
password = "123456"
expected_texts = ['Профиль', 'История заказов', 'Выход', 'Имя', 'Логин',
                  'Пароль', 'В этом разделе вы можете изменить свои персональные данные']

def open_account(driver):
    WebDriverWait(driver, 2).until(expected_conditions.element_to_be_clickable(
        (By.XPATH, "//p[@class='AppHeader_header__linkText__3q_va ml-2' and text()='Личный Кабинет']"))).click()
    WebDriverWait(driver, 2).until(expected_conditions.element_to_be_clickable((By.XPATH, "//button[text()='Сохранить']")))


def test_open_account_from_home_page(driver):
    driver.get("https://stellarburgers.nomoreparties.site/login")
    login_user(driver, email, password)
    open_account(driver)
    for text in expected_texts:
        assert text in driver.page_source

