import pytest
from selenium import webdriver

@pytest.fixture(autouse=True)
def setup_and_teardown():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get("https://www.saucedemo.com/")
    yield driver
    driver.quit()
