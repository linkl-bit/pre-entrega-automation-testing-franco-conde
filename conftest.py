import pytest
from selenium import webdriver
from utils import login

@pytest.fixture
def driver():
    driver=webdriver.Chrome()
    yield driver
    driver.quit()
#todo lo que viene despues del yield se ejecuta sin importar lo que haya pasado