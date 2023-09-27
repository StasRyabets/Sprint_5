from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

expected_texts = ['Соберите бургер', 'Булки', 'Соусы', 'Начинки']

def test_open_constructor_click_on_button(driver):
    driver.get("https://stellarburgers.nomoreparties.site/account")
    WebDriverWait(driver, 2).until(expected_conditions.element_to_be_clickable(
        (By.XPATH, '//p[text()="Конструктор"]'))).click()
    for text in expected_texts:
        assert text in driver.page_source

def test_open_constructor_click_on_logo(driver):
    driver.get("https://stellarburgers.nomoreparties.site/account")
    WebDriverWait(driver, 2).until(expected_conditions.element_to_be_clickable(
        (By.XPATH, '//*[@id="root"]/div/header/nav/div'))).click()
    for text in expected_texts:
        assert text in driver.page_source

def test_go_to_section_sauce(driver):
    driver.get("https://stellarburgers.nomoreparties.site")
    WebDriverWait(driver, 2).until(expected_conditions.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/main/section[1]/div[1]/div[2]'))).click()
    assert WebDriverWait(driver, 2).until(expected_conditions.visibility_of_element_located(
        (By.XPATH, '//*[@id="root"]/div/main/section[1]/div[1]/div[2][contains(@class,"current")]'))) is not None

def test_go_to_section_filling(driver):
    driver.get("https://stellarburgers.nomoreparties.site")
    WebDriverWait(driver, 2).until(expected_conditions.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/main/section[1]/div[1]/div[3]'))).click()
    assert WebDriverWait(driver, 2).until(expected_conditions.visibility_of_element_located(
        (By.XPATH, '//*[@id="root"]/div/main/section[1]/div[1]/div[3][contains(@class,"current")]'))) is not None
    
def test_go_to_section_bun(driver):
    driver.get("https://stellarburgers.nomoreparties.site")
    WebDriverWait(driver, 2).until(expected_conditions.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/main/section[1]/div[1]/div[3]'))).click()
    WebDriverWait(driver, 2).until(expected_conditions.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/main/section[1]/div[1]/div[1]'))).click()
    assert WebDriverWait(driver, 2).until(expected_conditions.visibility_of_element_located(
        (By.XPATH, '//*[@id="root"]/div/main/section[1]/div[1]/div[1][contains(@class,"current")]'))) is not None