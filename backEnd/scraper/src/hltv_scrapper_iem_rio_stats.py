import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pymongo import MongoClient
from banco import Banco
from inicia_selenium import iniciaselenium

# Conexão com o Mongodb
banco_de_dados = Banco.inicia_banco()
iem_rio = Banco.iem_rio(banco_de_dados)
iem_rio_partidas = Banco.iem_rio_partidas(banco_de_dados)


# Definindo os cards para extração
cards = []

# Acessar o banco e pegar as tabelas necessarias
matches = []
for match in iem_rio.find():
    matches.append(match)

n = 1

# Rodando cada partida
for match in matches:
    if match['numero_partida'] <= 8:
        # Iniciando o Selenium para cada partida
        driver = iniciaselenium.inicia()
        print("Chrome Initialized 1")

        # Entrando no link da partida
        driver.get(
            "https://www.hltv.org" + match['link_partida'])
        # Concorda com os cookies do site
        time.sleep(1)
        elemento = driver.find_element(
            By.XPATH, '//*[@id="CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll"]')
        driver.execute_script("arguments[0].click();", elemento)

        # Obtendo o html
        paginaatual = BeautifulSoup(driver.page_source, 'html.parser')

        # fechando o selenium para a primeira tela da partida
        driver.quit()

        # Indo para o status mais detalhados da partida
        link = paginaatual.find('div', {'class': 'matchstats'}).find(
            'div', {'class': 'flexbox nowrap stats-type'}).find('a').get('href')

        # Iniciando o Selenium para a pagina detalhada
        driver = iniciaselenium.inicia()
        print("Chrome Initialized 2")

        driver.get(
            "https://www.hltv.org" + link)
        # Concorda com os cookies do site
        time.sleep(1)
        elemento = driver.find_element(
            By.XPATH, '//*[@id="CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll"]')
        driver.execute_script("arguments[0].click();", elemento)

        # Obtendo o html
        paginadetalhada = BeautifulSoup(driver.page_source, 'html.parser')

        driver.quit()

        # Retirando os dados necessarios
        card = {}

        card['adversarios'] = match['team_1'] + ' X ' + match['team_2']
        card['team_1'] = match['team_1']
        card['team_2'] = match['team_2']

        card['team_victory'] = match['team_victory']
        card['victory_score'] = match['victory_score']
        card['team_defeat'] = match['team_defeat']
        card['defeat_score'] = match['defeat_score']

        card['partida'] = []
        if match['numero_de_rodadas'] > 1:
            # entrando em cada mapa e sabendo quais são os detalhes
            rodadas = paginadetalhada.find('div', {'class': 'contentCol'}).find(
                'div', {'class': 'stats-section'}).find(
                'div', {'class': 'columns'}).find_all('a')
            mapaatual = 1
            for rodada in rodadas:
                partida = {}
                # Iniciando o Selenium
                driver = iniciaselenium.inicia()
                print("Chrome Initialized 3")

                driver.get(
                    "https://www.hltv.org" + rodada.get('href'))
                # Concorda com os cookies do site
                time.sleep(1)
                elemento = driver.find_element(
                    By.XPATH, '//*[@id="CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll"]')
                driver.execute_script("arguments[0].click();", elemento)

                paginastatusdetalhada = BeautifulSoup(
                    driver.page_source, 'html.parser')

                partida['placar_vencedor'] = paginastatusdetalhada.find('div', {'class': 'contentCol'}).find(
                    'div', {'class': 'wide-grid'}).find('div', {'class': 'col'}).div.div.find('div', {'class': 'bold won'}).getText()
                partida['placar_perdedor'] = paginastatusdetalhada.find('div', {'class': 'contentCol'}).find(
                    'div', {'class': 'wide-grid'}).find('div', {'class': 'col'}).div.div.find('div', {'class': 'bold lost'}).getText()

                if mapaatual == 1:
                    partida['Mapa'] = 'Resumo de todas'
                else:
                    partida['Mapa'] = paginastatusdetalhada.find('div', {'class': 'contentCol'}).find(
                        'div', {'class': 'wide-grid'}).find('div', {'class': 'col'}).div.div.text().getText()

                partida['Team rating'] = paginastatusdetalhada.find('div', {'class': 'contentCol'}).find(
                    'div', {'class': 'wide-grid'}).find('div', {'class': 'col'}).div.div.findNextSibling().find('div', {'class': 'right'}).getText()

                partida['First kills'] = paginastatusdetalhada.find('div', {'class': 'contentCol'}).find(
                    'div', {'class': 'wide-grid'}).find('div', {'class': 'col'}).div.div.findNextSibling().findNextSibling().find('div', {'class': 'right'}).getText()

                partida['Clutches won'] = paginastatusdetalhada.find('div', {'class': 'contentCol'}).find(
                    'div', {'class': 'wide-grid'}).find('div', {'class': 'col'}).div.div.findNextSibling().findNextSibling().findNextSibling().find('div', {'class': 'right'}).getText()

                card['partida'].append(partida)
                mapaatual+1

                driver.quit()
        elif match['numero_de_rodadas'] == 1:
            partida = {}

            partida['placar_vencedor'] = paginadetalhada.find('div', {'class': 'contentCol'}).find(
                'div', {'class': 'wide-grid'}).find('div', {'class': 'col'}).div.div.find('div', {'class': 'bold won'}).getText()
            partida['placar_perdedor'] = paginadetalhada.find('div', {'class': 'contentCol'}).find(
                'div', {'class': 'wide-grid'}).find('div', {'class': 'col'}).div.div.find('div', {'class': 'bold lost'}).getText()

            partida['Team rating'] = paginadetalhada.find('div', {'class': 'contentCol'}).find(
                'div', {'class': 'wide-grid'}).find('div', {'class': 'col'}).div.div.findNextSibling().find('div', {'class': 'right'}).getText()

            partida['First kills'] = paginadetalhada.find('div', {'class': 'contentCol'}).find(
                'div', {'class': 'wide-grid'}).find('div', {'class': 'col'}).div.div.findNextSibling().findNextSibling().find('div', {'class': 'right'}).getText()

            partida['Clutches won'] = paginadetalhada.find('div', {'class': 'contentCol'}).find(
                'div', {'class': 'wide-grid'}).find('div', {'class': 'col'}).div.div.findNextSibling().findNextSibling().findNextSibling().find('div', {'class': 'right'}).getText()

            card['partida'].append(partida)

        iem_rio_partidas.insert_one(card)
