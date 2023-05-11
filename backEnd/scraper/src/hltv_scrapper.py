import time
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from banco import Banco
from inicia_selenium import iniciaselenium

# Conexão com o Mongodb
banco_de_dados = Banco.inicia_banco()
teams = Banco.teams(banco_de_dados)

# Iniciando o Selenium
driver = iniciaselenium.inicia()
print("Chrome Initialized")

# Entrando no site do hltv
driver.get("https://www.hltv.org")

# Concorda com os cookies do site
time.sleep(2)
elemento = driver.find_element(
    By.XPATH, '//*[@id="CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll"]')
driver.execute_script("arguments[0].click();", elemento)

print("teste 1")

# Obtendo o html
soup = BeautifulSoup(driver.page_source, 'html.parser')

time.sleep(50)

# Fechando o Driver
driver.quit()
