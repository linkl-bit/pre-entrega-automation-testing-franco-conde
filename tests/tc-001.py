from selenium.webdriver.common.by import By
from selenium import webdriver
from utils import login

def test_login_validado(driver):
    try:
        login(driver,"standard_user","secret_sauce")

        assert "/inventory.html" in driver.current_url, "No se redirigio correctamente al inventario."

    #guardo en una variable el posible error
    except Exception as e: 
        print(f"Error en Test-Case-001: {e}")
        raise #dejo un registro de que el test fallo
    finally:
        driver.quit()