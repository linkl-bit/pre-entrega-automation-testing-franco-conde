from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_login_invalido():
    driver = webdriver.Chrome() 

    try:
        driver.get("https://www.saucedemo.com/")
        time.sleep(1)

        driver.find_element(By.ID,"user-name").send_keys("no_user")
        driver.find_element(By.ID,"password").send_keys("no_123")
        driver.find_element(By.ID,"login-button").click()
        time.sleep(2)

        #valido si sigue en la misma pagina
        assert "/inventory.html" not in driver.current_url, "Se redirigio al inventario con credenciales invalidas."

        #convierto en string el boton de error
        #valido si aparece el mensaje de error en el string
        mensaje=driver.find_element(By.CLASS_NAME,"error-message-container").text
        assert "Username and password do not match" in mensaje, "El mensaje de error no fue el esperado."

        print("Login invalido verificado correctamente.")

    except Exception as e:
        print(f"Error en Test-Case-002: {e}")
        raise

    finally:
        driver.quit()