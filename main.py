# Teste de automação de uma compra no site da Amazon
# Por: Flávio Mota Gomes

# Importações
import pytest
import time
import json

# Importações do Selenium, ferramenta utilizada para o teste
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

# Definição do driver. Este teste usa o Google Chrome
driver = webdriver.Chrome()

# URL inicial do teste
driver.get("https://www.amazon.com.br/")

# Definição do tamanho da janela
driver.set_window_size(1382, 744)

# Clique na aba de pesquisa de produtos presente no site da Amazon
driver.find_element(By.ID, "twotabsearchtextbox").click()

# Insere-se o valor "alexa" na busca de produto
driver.find_element(By.ID, "twotabsearchtextbox").send_keys("alexa")

# Clica-se no botão de pesquisa. Uma alternativa a isto seria teclar "enter"
driver.find_element(By.ID, "nav-search-submit-button").click()

# Seleção do produto na página
driver.find_element(By.CSS_SELECTOR, ".sg-col-4-of-12:nth-child(3) .a-size-base-plus:nth-child(1)").click()

# Clica-se para adicionar o produto ao carrinho de compras
driver.find_element(By.ID, "add-to-cart-button").click()

# A pagina da Amazon naturalmente realiza a sugestão de compra de outro produto junto ao escolhido.
# Aqui, clicamos para não fazer esta compra casada
driver.find_element(By.CSS_SELECTOR, "#a-autoid-11 .a-button-input").click()

# Finalização da compra, fechando o pedido no carrinho
element = driver.find_element(By.ID, "hlb-ptc-btn-native")
actions = ActionChains(driver)
actions.move_to_element(element).perform()
driver.find_element(By.ID, "hlb-ptc-btn-native").click()