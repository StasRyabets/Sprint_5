from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from data import *
from utils import *


def test_open_account(driver):
    driver.get(login_page)
    login_user(driver, valid_email, valid_password)
    open_account(driver)
    for text in texts_on_account_page:
        assert text in driver.page_source
