import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from utils import login

@pytest.fixture
def driver():
    chrome_opt = Options()
    chrome_opt.add_argument("--incognito")
    driver = webdriver.Chrome(options=chrome_opt)
    yield driver
    driver.quit()