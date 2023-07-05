import time
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from banco import Banco
from inicia_selenium import iniciaselenium

# Conexão com o Mongodb
banco_de_dados = Banco.inicia_banco()
teamss = Banco.teams(banco_de_dados)
partidass = Banco.iem_rio_partidas(banco_de_dados)
teams_details = Banco.teams_details(banco_de_dados)


def adicionaPartida(name, link, rating, banco):

    if banco.find_one({"name": name}) == None:
        card = {}
        card['name'] = name
        # Link do time
        card['linktime'] = link

        # Rating do time
        card['rating'] = rating

        card['forca'] = 500

        card['partidas'] = []

        banco.insert_one(card)


def updatePartida(name, partida, banco):
    perdeu = banco.find_one({"name": partida['team_defeat']})
    ganhou = banco.find_one({"name": partida['team_victory']})
    if partida['team_victory'] == name:
        if ganhou['forca'] >= perdeu['forca']:
            novaforca = ganhou['forca'] + 10
            print(novaforca)
            return novaforca
        elif ganhou['forca'] <= perdeu['forca']:
            novaforca = ganhou['forca'] + 20
            print(novaforca)
            return novaforca
    else:
        if perdeu['forca'] >= ganhou['forca']:
            novaforca = perdeu['forca'] - 20
            print(novaforca)
            return novaforca
        elif perdeu['forca'] <= ganhou['forca']:
            novaforca = perdeu['forca'] - 10
            print(novaforca)
            return novaforca


# Declarando variável cards e imagens
partidas = partidass.find()
cards = []
i = len(partidas)

for partida in partidas:
    print(partida['team_1'] + " vs " +
          partida['team_2'] + " Contagem =  " + str(i))
    teams = teamss.find()
    for team in teams:
        if partida['team_1'] == team['name']:
            adicionaPartida(
                team['name'], team['linktime'], team['rating'], teams_details)
        elif partida['team_2'] == team['name']:
            adicionaPartida(
                team['name'], team['linktime'], team['rating'], teams_details)
    i = i - 1

# Coletando as informações dos CARDS
for partida in partidas:
    print(partida['team_1'] + " vs " +
          partida['team_2'] + " Contagem =" + str(i))
    teams_detailss = teams_details.find()
    for team in teams_detailss:
        if partida['team_1'] == team['name']:
            novaforca = updatePartida(team['name'], partida, teams_details)
            teams_details.update_one(
                {'name': team['name']}, {"$set": {"forca": novaforca}})
            teams_details.update_one({'name': team['name']}, {"$push": {
                                     "partidas": partida}})
            print("Achou o time 1 da partida " +
                  str(i) + " Nova força " + str(novaforca))
        elif partida['team_2'] == team['name']:
            novaforca = updatePartida(team['name'], partida, teams_details)
            teams_details.update_one(
                {'name': team['name']}, {"$set": {"forca": novaforca}})
            teams_details.update_one({'name': team['name']}, {"$push": {
                                     "partidas": partida}})
            print("Achou o time 2 da partida " +
                  str(i) + " Nova força " + str(novaforca))
    i = i - 1
