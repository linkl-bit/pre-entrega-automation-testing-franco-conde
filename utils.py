#funciones a utilizar en tests
from selenium.webdriver.common.by import By
import time

def login(driver,username,password):
    driver.get("https://www.saucedemo.com/") #pagina a testear

    #selecciono los elementos y envio las credenciales
    driver.find_element(By.ID,"user-name").send_keys(username) 
    driver.find_element(By.ID,"password").send_keys(password)
    #clickeo boton login
    driver.find_element(By.ID,"login-button").click() 
    time.sleep(2)