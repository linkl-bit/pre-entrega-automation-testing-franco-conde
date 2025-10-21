from selenium.webdriver.common.by import By
from selenium import webdriver
from utils import login

def test_inventario(driver):
    try:
        login(driver,"standard_user","secret_sauce")

        assert driver.title == "Swag Labs"
        productos=driver.find_elements(By.CLASS_NAME,"inventory_item")
        assert len(productos)>0, "No hay productos visibles en la pagina."
        assert driver.find_element(By.CLASS_NAME,"product_sort_container"), "No se encontro el boton de filtro."
        assert driver.find_element(By.CLASS_NAME,"bm-burger-button"), "No se encontro el boton de menu."
    
    except Exception as e:
        print(f"Error en test_inventory: {e}")
        raise
    finally:
        driver.quit()