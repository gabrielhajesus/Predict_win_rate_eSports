import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from pymongo import MongoClient
from urllib.request import Request, urlopen, urlretrieve
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

print("retirou os cookies")

driver.get(
    "https://www.hltv.org/stats/teams?startDate=2022-10-28&endDate=2023-04-28")

# Obtendo o html
paginainicial = BeautifulSoup(driver.page_source, 'html.parser')

quantidadeDeTimes = paginainicial.find('div', {'class': "filter-column-con"})

with open("saida_texto.txt", "w", encoding="utf-8") as arquivo:
    arquivo.write(quantidadeDeTimes)


driver.quit()
