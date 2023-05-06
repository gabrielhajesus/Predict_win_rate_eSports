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
driver.get(
    "https://www.hltv.org/stats/teams?startDate=2022-10-28&endDate=2023-04-28&minMapCount=30")

# Concorda com os cookies do site
time.sleep(1)
elemento = driver.find_element(
    By.XPATH, '//*[@id="CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll"]')
driver.execute_script("arguments[0].click();", elemento)


# Obtendo o html
paginainicial = BeautifulSoup(driver.page_source, 'html.parser')

driver.quit()

tableTeams = paginainicial.find('table').find('tbody').find_all('tr')
print("pegou a tabela")

# Declarando variável cards e imagens
cards = []

# Coletando as informações dos CARDS
for team in tableTeams:
    card = {}

    # Nome do time
    card['name'] = team.find(
        'td', {'class': 'teamCol-teams-overview'}).getText()

    # Link do time
    card['linktime'] = team.find('a').get('href')

    # Rating do time
    card['rating'] = team.find('td', {'class': 'ratingCol'}).getText()

    cards.append(card)

teams.insert_many(cards)
