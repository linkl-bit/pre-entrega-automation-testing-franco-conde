from selenium.webdriver.common.by import By
from selenium import webdriver
from utils import login

def test_carrito(driver):
    try:
        login(driver,"standard_user","secret_sauce")
        
        #valido existencia de producto Backpack, buscando directamente su boton añair al carrito y luego lo clickeo.
        boton_backpack=driver.find_element(By.ID,"add-to-cart-sauce-labs-backpack")
        assert boton_backpack is not None, "Botón 'Add to cart' no encontrado."
        boton_backpack.click()

        #busco botón de carrito y valido su existencia, luego, lo clickeo
        boton_carrito=driver.find_element(By.CLASS_NAME,"shopping_cart_link")
        assert boton_carrito is not None, "Botón de 'Carrito' no encontrado."
        boton_carrito.click()

        #verifico que al clickear el carrito, me redirija a la url correcta
        assert "/cart.html" in driver.current_url, "No se redirigio correctamente al carro de compras."
        
        #verifico que el nombre del producto es el mismo que elegí previamente
        nombre_producto=driver.find_element(By.CLASS_NAME,"inventory_item_name").text
        assert nombre_producto=="Sauce Labs Backpack", "El nombre del producto no es el esperado."

    except Exception as e:
        print(f"Error en Test-Case-004: {e}")
        raise
