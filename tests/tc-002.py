from selenium import webdriver
from selenium.webdriver.common.by import By
from utils import login

def test_login_invalido(driver):
    driver = webdriver.Chrome() 

    try:
        login(driver,"no_user","no_123")
        #valido si sigue en la misma pagina
        assert "/inventory.html" not in driver.current_url, "Se redirigio al inventario con credenciales invalidas."
        #convierto en string el boton de error y valido si aparece el mensaje de error en el string
        mensaje=driver.find_element(By.CLASS_NAME,"error-message-container").text
        assert "Username and password do not match" in mensaje, "El mensaje de error no fue el esperado."

    except Exception as e:
        print(f"Error en Test-Case-002: {e}")
        raise