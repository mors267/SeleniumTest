import time
import pytest
from selenium.webdriver.common.by import By


class TestLoginPage:
    def test_valid_login(self, driver):
        driver.get("https://www.saucedemo.com/")
        # time.sleep(2)

        # Type username
        username_input = driver.find_element(By.ID, "user-name")
        username_input.send_keys("standard_user")

        # Type password
        password_input = driver.find_element(By.ID, "password")
        password_input.send_keys("secret_sauce")

        # Click on the login button
        login_btn = driver.find_element(By.ID, "login-button")
        login_btn.click()

        # URL Validation
        actual_url = driver.current_url
        assert actual_url == "https://www.saucedemo.com/inventory.htmls"

        # time.sleep(2)
