import pytest
from selenium import webdriver


@pytest.fixture
def set_driver():
    driver = webdriver.Chrome()
    driver.get('https://www.ketangpai.com/User/login.html')
    driver.maximize_window()
    yield driver
    driver.quit()