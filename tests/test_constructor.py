from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from data import *
from locators import *


def test_open_constructor_click_on_button(driver):
    driver.get(account_page)
    WebDriverWait(driver, 2).until(expected_conditions.element_to_be_clickable(
        (By.XPATH, constructor_button))).click()
    for text in texts_on_constructor_page:
        assert text in driver.page_source


def test_open_constructor_click_on_logo(driver):
    driver.get(account_page)
    WebDriverWait(driver, 2).until(expected_conditions.element_to_be_clickable(
        (By.XPATH, constructor_logo))).click()
    for text in texts_on_constructor_page:
        assert text in driver.page_source


def test_go_to_section_sauce(driver):
    driver.get(home_page)
    WebDriverWait(driver, 2).until(
        expected_conditions.element_to_be_clickable((By.XPATH, sauce_button))).click()
    assert WebDriverWait(driver, 2).until(expected_conditions.visibility_of_element_located(
        (By.XPATH, f'{sauce_button}{current_atribute}'))) is not None


def test_go_to_section_filling(driver):
    driver.get(home_page)
    WebDriverWait(driver, 2).until(expected_conditions.element_to_be_clickable(
        (By.XPATH, filling_button))).click()
    assert WebDriverWait(driver, 2).until(expected_conditions.visibility_of_element_located(
        (By.XPATH, f'{filling_button}{current_atribute}'))) is not None


def test_go_to_section_bun(driver):
    driver.get(home_page)
    WebDriverWait(driver, 2).until(expected_conditions.element_to_be_clickable(
        (By.XPATH, filling_button))).click()
    WebDriverWait(driver, 2).until(
        expected_conditions.element_to_be_clickable((By.XPATH, bun_button))).click()
    assert WebDriverWait(driver, 2).until(expected_conditions.visibility_of_element_located(
        (By.XPATH, f'{bun_button}{current_atribute}'))) is not None
