import pytest
from selenium import webdriver 
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.wait import WebDriverWait 
from selenium.webdriver.support import expected_conditions 
 
email = "stasriabets1042@ya.uz" 
password = "123456" 
 
@pytest.fixture(scope="function")
def login_user():
    driver = webdriver.Chrome() 
    driver.get("https://stellarburgers.nomoreparties.site") 
 
    WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable( 
        (By.XPATH, "//button[text()='Войти в аккаунт']"))).click() 
 
    WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable( 
        (By.XPATH, "//button[text()='Войти']"))) 
    driver.find_element( 
        By.XPATH, "//label[text()='Email']/following-sibling::input[@type='text']").send_keys(email) 
    driver.find_element( 
        By.XPATH, "//label[text()='Пароль']/following-sibling::input[@type='password']").send_keys(password) 
    driver.find_element(By.XPATH, "//button[text()='Войти']").click() 

    yield driver

    driver.quit()
 
 
def test_login_from_home_page(login_user): 
    button = WebDriverWait(login_user, 10).until(expected_conditions.visibility_of_element_located( 
        (By.XPATH, "//button[text()='Оформить заказ']"))) 
    assert button.text == "Оформить заказ" 
 
 
def test_login_from_account_page(login_user): 
    login_user.get("https://stellarburgers.nomoreparties.site/account") 
 
    button = WebDriverWait(login_user, 10).until(expected_conditions.visibility_of_element_located( 
        (By.XPATH, "//button[text()='Оформить заказ']"))) 
    assert button.text == "Оформить заказ"