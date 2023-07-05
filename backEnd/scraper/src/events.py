import time
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from banco import Banco
import undetected_chromedriver as uc
import chromedriver_autoinstaller

# Conexão com o Mongodb
banco_de_dados = Banco.inicia_banco()
campeonatos = Banco.campeonatos(banco_de_dados)


# Entrando no site do hltv
# 1 https://www.hltv.org/events/6862/esl-pro-league-season-17
# 2 https://www.hltv.org/events/7085/betboom-playlist-urbanistic-2023
# 3 https://www.hltv.org/events/6864/iem-rio-2023
# 4 https://www.hltv.org/events/7122/brazy-party-2023
# 5 https://www.hltv.org/events/6793/blasttv-paris-major-2023
# 6 https://www.hltv.org/events/6861/iem-dallas-2023
# 7 https://www.hltv.org/events/6972/blast-premier-spring-final-2023
# 8 https://www.hltv.org/events/6867/esl-challenger-katowice-2023


eventos = ['/events/6862/esl-pro-league-season-17', '/events/7085/betboom-playlist-urbanistic-2023', '/events/6864/iem-rio-2023', '/events/7122/brazy-party-2023',
           '/events/6793/blasttv-paris-major-2023', '/events/6861/iem-dallas-2023', '/events/6972/blast-premier-spring-final-2023', '/events/6867/esl-challenger-katowice-2023']

for evento in eventos:
    # Iniciando o emulador idetectavel do google
    version_main = int(
        chromedriver_autoinstaller.get_chrome_version().split(".")[0])
    options = uc.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--headless')
    driver = uc.Chrome(use_subprocess=True, options=options,
                       version_main=version_main)
    driver.maximize_window()
    print("Chrome Initialized")
    driver.get(
        "https://www.hltv.org" + evento)

    # Concorda com os cookies do site
    time.sleep(1)
    elemento = driver.find_element(
        By.XPATH, '//*[@id="CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll"]')
    driver.execute_script("arguments[0].click();", elemento)

    # Obtendo o html
    paginainicial = BeautifulSoup(driver.page_source, 'html.parser')

    caminho = paginainicial.find(
        'div', {'class': 'event-hub-bottom'}).a.find_next_sibling().get('href')

    driver.get(
        "https://www.hltv.org" + caminho)

    paginainicial = BeautifulSoup(driver.page_source, 'html.parser')

    driver.quit()

    # Pegando a tabela inicial dos jogos
    resultados = paginainicial.find(
        'div', {'class': 'results-all'}).find_all('div', {'class': 'results-sublist'})

    cards = []
    partidas = []

    # Separando cada jogo das sub-tabelas

    for resultado in resultados:
        partidass = resultado.find_all('div', {'class': 'result-con'})
        for partida in partidass:
            partidas.append(partida)

    contador_partidas = len(partidas)

    # Retirando os dados necessarios

    for partida in partidas:
        card = {}

        card['campeonato'] = paginainicial.find(
            'div', {"class": "event-hub-title"}).get_text()

        # Numero da partida
        card['numero_partida'] = contador_partidas
        contador_partidas = contador_partidas - 1

        # Oponentes - Nomes dos times
        team_1 = partida.find('table').find(
            'tbody').find('div', {'class': "line-align team1"})

        card['team_1'] = team_1.getText().replace('\n', '')

        team_2 = partida.find('table').find(
            'tbody').find('div', {'class': "line-align team2"})

        card['team_2'] = team_2.getText().replace('\n', '')

        # Quem ganhou - Resultado
        scoreteam_1 = partida.find('table').find(
            'td', {'class': 'result-score'}).span.getText().replace('\n', '')

        scoreteam_2 = partida.find('table').find(
            'td', {'class': 'result-score'}).span.findNextSibling().getText().replace('\n', '')

        if int(scoreteam_1) > int(scoreteam_2):
            card['team_victory'] = team_1.getText().replace('\n', '')
            card['victory_score'] = scoreteam_1
            card['team_defeat'] = team_2.getText().replace('\n', '')
            card['defeat_score'] = scoreteam_2
        elif int(scoreteam_1) < int(scoreteam_2):
            card['team_victory'] = team_2.getText().replace('\n', '')
            card['victory_score'] = scoreteam_2
            card['team_defeat'] = team_1.getText().replace('\n', '')
            card['defeat_score'] = scoreteam_1

        if int(scoreteam_1) == 3 or int(scoreteam_2) == 3:
            card['numero_de_rodadas'] = int(scoreteam_1) + int(scoreteam_2)
        elif int(scoreteam_1) + int(scoreteam_2) > 3:
            card['numero_de_rodadas'] = 1
        else:
            card['numero_de_rodadas'] = int(scoreteam_1) + int(scoreteam_2)

        # link da partida

        card['link_partida'] = partida.find('a').get('href')
        cards.append(card)

    campeonatos.insert_many(cards)
