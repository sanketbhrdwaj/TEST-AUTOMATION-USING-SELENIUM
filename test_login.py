import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://practicetestautomation.com/practice-test-login/")
    yield driver
    driver.quit()

def test_login_valid_user(driver):
    # Login
    driver.find_element(By.ID, "username").send_keys("student")
    driver.find_element(By.ID, "password").send_keys("Password123")
    driver.find_element(By.ID, "submit").click()
    time.sleep(2)

    # Verify login success
    success_text = driver.find_element(By.TAG_NAME, "h1").text
    assert success_text == "Logged In Successfully"

    # Logout
    driver.find_element(By.LINK_TEXT, "Log out").click()
    time.sleep(2)

    # Confirm redirection
    assert "practice-test-login" in driver.current_url
