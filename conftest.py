import pytest
from selenium import webdriver

@pytest.fixture(scope="function") # @pytest.fixture(scope="session") [w/o browser restart. Fixture will execute once per session!]
def browser():
    driver = webdriver.Chrome(executable_path="chromedriver.exe")
    yield driver
    driver.quit()
