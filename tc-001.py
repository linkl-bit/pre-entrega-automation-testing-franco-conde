from selenium import webdriver
from selenium.webdriver.common.by import By #para selectores
import time

def test_login_valido():
    driver = webdriver.Chrome() #navegador a utilizar

    try: 
        driver.get("https://www.saucedemo.com/") #pagina a testear
        time.sleep(1)

        #selecciono los elementos y envio las credenciales
        driver.find_element(By.ID,"user-name").send_keys("standard_user") 
        driver.find_element(By.ID,"password").send_keys("secret_sauce")
        driver.find_element(By.ID,"login-button").click() #clickeo boton login
        time.sleep(2)

        #valido si la pagina que ingresamos es la correcta
        #se busca el texto entre comillas en el url actual
        assert "/inventory.html" in driver.current_url, "No se redirigio correctamente al inventario."
        
        print("Login valido verificado correctamente.")
        
    #guardo en una variable el posible error
    except Exception as e: 
        print(f"Error en Test-Case-001: {e}")
        raise #dejo un registro de que el test fallo

    #conj de instrucciones que se ejecutan luego de haber intentado ejecutar el try o haya tenido un error
    finally: 
        driver.quit()