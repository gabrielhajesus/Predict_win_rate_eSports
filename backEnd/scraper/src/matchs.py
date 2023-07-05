import time
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from banco import Banco
from inicia_selenium import iniciaselenium
import undetected_chromedriver as uc
import chromedriver_autoinstaller

# Conexão com o Mongodb
banco_de_dados = Banco.inicia_banco()
campeonatos = Banco.campeonatos(banco_de_dados)
partidas = Banco.partidas(banco_de_dados)

# Definindo os cards para extração
cards = []

# Acessar o banco e pegar as tabelas necessarias
matches = []
for match in campeonatos.find():
    matches.append(match)

n = 1

contador_de_paginas = 0
# Rodando cada partida
for match in matches:

    if contador_de_paginas < 150:
        # Iniciando o Selenium para cada partida
        driver = iniciaselenium.inicia()
        print("Do campeonato " + match['campeonato'] +
              " partida numero = " + str(match['numero_partida']))

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

        driver = iniciaselenium.inicia()

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

        card['team_1'] = str(match['team_1']).replace(
            '\n', '')
        card['team_1_img'] = paginadetalhada.find('div', {'class': 'contentCol'}).find(
            'div', {'class': 'wide-grid'}).div.div.div.div.findNextSibling().img.get('src')
        card['team_2'] = str(match['team_2']).replace('\n', '')
        card['team_2_img'] = paginadetalhada.find('div', {'class': 'contentCol'}).find(
            'div', {'class': 'wide-grid'}).div.div.div.div.findNextSibling().findNextSibling().img.get('src')

        print("Pagina detalha da partida " +
              card['team_1'] + " X " + card['team_2'])

        card['team_victory'] = str(match['team_victory']).replace('\n', '')
        card['victory_score'] = match['victory_score'].replace(' ', '')

        card['team_defeat'] = str(match['team_defeat']).replace('\n', '')
        card['defeat_score'] = match['defeat_score'].replace(' ', '')

        card['partida'] = []

        if match['numero_de_rodadas'] > 1:
            # entrando em cada mapa e sabendo quais são os detalhes
            rodadas = paginadetalhada.find('div', {'class': 'contentCol'}).find(
                'div', {'class': 'stats-section'}).find('div', {"class": "stats-match-maps"}).find(
                'div', {'class': 'columns'}).find_all('a')
            print((len(rodadas)))
            mapaatual = 1
            for rodada in rodadas:
                if mapaatual > 1:
                    partida = {}

                    driver = iniciaselenium.inicia()
                    print("Pegando os dados do mapa" + str(mapaatual))

                    driver.get(
                        "https://www.hltv.org" + rodada.get('href'))
                    # Concorda com os cookies do site
                    time.sleep(1)
                    elemento = driver.find_element(
                        By.XPATH, '//*[@id="CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll"]')
                    driver.execute_script("arguments[0].click();", elemento)

                    paginastatusdetalhada = BeautifulSoup(
                        driver.page_source, 'html.parser')

                    # placar
                    partida['placar'] = paginastatusdetalhada.find('div', {'class': 'contentCol'}).find(
                        'div', {'class': 'wide-grid'}).find('div', {'class': 'col'}).div.div.findNextSibling().find('div', {'class': 'right'}).getText()

                    # nome do mapa
                    nome_do_mapa = paginastatusdetalhada.find('div', {'class': 'contentCol'}).find(
                        'div', {'class': 'wide-grid'}).find('div', {'class': 'col'}).div.div.getText()
                    nome_do_mapa = nome_do_mapa.split('\n')[2]
                    partida['Mapa'] = nome_do_mapa

                    # team rating
                    partida['team_rating'] = paginastatusdetalhada.find('div', {'class': 'contentCol'}).find(

                        # first kill
                        'div', {'class': 'wide-grid'}).find('div', {'class': 'col'}).div.div.findNextSibling().findNextSibling().find('div', {'class': 'right'}).getText()
                    partida['first_kills'] = paginastatusdetalhada.find('div', {'class': 'contentCol'}).find(
                        'div', {'class': 'wide-grid'}).find('div', {'class': 'col'}).div.div.findNextSibling().findNextSibling().findNextSibling().find('div', {'class': 'right'}).getText()

                    # clutches
                    partida['clutches_won'] = paginastatusdetalhada.find('div', {'class': 'contentCol'}).find(
                        'div', {'class': 'wide-grid'}).find('div', {'class': 'col'}).div.div.findNextSibling().findNextSibling().findNextSibling().findNextSibling().find('div', {'class': 'right'}).getText()

                    card['partida'].append(partida)
                    mapaatual = mapaatual+1
                    driver.quit()
                else:
                    mapaatual = mapaatual + 1
        elif match['numero_de_rodadas'] == 1:

            print("Pegando os dados do mapa")
            partida = {}
            # placar
            partida['placar'] = paginadetalhada.find('div', {'class': 'contentCol'}).find(
                'div', {'class': 'wide-grid'}).find('div', {'class': 'col'}).div.div.findNextSibling().find('div', {'class': 'right'}).getText()

            # nome do mapa
            nome_do_mapa = paginadetalhada.find('div', {'class': 'contentCol'}).find(
                'div', {'class': 'wide-grid'}).find('div', {'class': 'col'}).div.div.getText()
            nome_do_mapa = nome_do_mapa.split('\n')[2]
            partida['Mapa'] = nome_do_mapa

            # team rating
            partida['team_rating'] = paginadetalhada.find('div', {'class': 'contentCol'}).find(
                'div', {'class': 'wide-grid'}).find('div', {'class': 'col'}).div.div.findNextSibling().find('div', {'class': 'right'}).getText()

            # first kill
            partida['first_kills'] = paginadetalhada.find('div', {'class': 'contentCol'}).find(
                'div', {'class': 'wide-grid'}).find('div', {'class': 'col'}).div.div.findNextSibling().findNextSibling().find('div', {'class': 'right'}).getText()

            # clutches
            partida['clutches_won'] = paginadetalhada.find('div', {'class': 'contentCol'}).find(
                'div', {'class': 'wide-grid'}).find('div', {'class': 'col'}).div.div.findNextSibling().findNextSibling().findNextSibling().find('div', {'class': 'right'}).getText()

            card['partida'].append(partida)
        partidas.insert_one(card)
        contador_de_paginas = contador_de_paginas + 1


driver.quit()
