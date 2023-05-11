import time
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from banco import Banco
from inicia_selenium import iniciaselenium

# Conexão com o Mongodb
banco_de_dados = Banco.inicia_banco()
iem_rio = Banco.iem_rio(banco_de_dados)

# Iniciando o Selenium
driver = iniciaselenium.inicia()
print("Chrome Initialized")

# Entrando no site do hltv
driver.get(
    "https://www.hltv.org/results?event=6864")

# Concorda com os cookies do site
time.sleep(1)
elemento = driver.find_element(
    By.XPATH, '//*[@id="CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll"]')
driver.execute_script("arguments[0].click();", elemento)

# Obtendo o html
paginainicial = BeautifulSoup(driver.page_source, 'html.parser')

driver.quit()

# Pegando a tabela inicial dos jogos
resultados = paginainicial.find(
    'div', {'class': 'results-all'}).find_all('div', {'class': 'results-sublist'})

cards = []
contador_partidas = 29
partidas = []

# Separando cada jogo das sub-tabelas

for resultado in resultados:
    partidass = resultado.find_all('div', {'class': 'result-con'})
    for partida in partidass:
        partidas.append(partida)

# Retirando os dados necessarios

for partida in partidas:
    card = {}

    # Numero da partida
    card['numero_partida'] = contador_partidas
    contador_partidas = contador_partidas - 1

    # Oponentes - Nomes dos times
    team_1 = partida.find('table').find(
        'tbody').find('div', {'class': "line-align team1"})

    card['team_1'] = team_1.getText()

    team_2 = partida.find('table').find(
        'tbody').find('div', {'class': "line-align team2"})

    card['team_2'] = team_2.getText()

    # Quem ganhou - Resultado
    scoreteam_1 = partida.find('table').find(
        'td', {'class': 'result-score'}).span.getText()

    scoreteam_2 = partida.find('table').find(
        'td', {'class': 'result-score'}).span.findNextSibling().getText()

    if int(scoreteam_1) > int(scoreteam_2):
        card['team_victory'] = team_1.getText()
        card['victory_score'] = scoreteam_1
        card['team_defeat'] = team_2.getText()
        card['defeat_score'] = scoreteam_2
    elif int(scoreteam_1) < int(scoreteam_2):
        card['team_victory'] = team_2.getText()
        card['victory_score'] = scoreteam_2
        card['team_defeat'] = team_1.getText()
        card['defeat_score'] = scoreteam_1

    if int(scoreteam_1) == 3:
        card['numero_de_rodadas'] = int(scoreteam_1) + int(scoreteam_2)
    elif int(scoreteam_1) + int(scoreteam_2) > 3:
        card['numero_de_rodadas'] = 1
    else:
        card['numero_de_rodadas'] = int(scoreteam_1) + int(scoreteam_2)

    # link da partida

    card['link_partida'] = partida.find('a').get('href')
    cards.append(card)

iem_rio.insert_many(cards)
