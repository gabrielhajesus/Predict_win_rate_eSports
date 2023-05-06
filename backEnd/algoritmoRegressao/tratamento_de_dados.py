from banco import Banco

from pymongo import MongoClient
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd

# Organizar os dados para colocar no dataset
# Separar os dados por time
# Fazer uma tabela em que cada time vai ter varios rounds e em cada um desses rounds vai conter as informações se win ou perdeu, o team rating, o first kill e o clutches_won
# caracteristicas dos dados
# win ou perdeu será binario
# team rating é a diferença entre kill e death do time todo
# o first kill serão as primeiras kills do jogo, essas kills representam uma vantagem na jogo
# o clutches_won são rodadas na qual o time win matando todos os outros do outro time

# Pegar os dados
banco_de_dados = Banco.inicia_banco()
iem_rio_partidas = Banco.iem_rio_partidas(banco_de_dados)
pd.set_option('display.max_rows', 200)


# Acessa a Collection que guarda as informações para o dataset especifico

dataset_iem_rio = Banco.dataset_iem_rio(banco_de_dados)

# Guarda todos os dados da Collection em uma lista
teams_partidas = []
for match in iem_rio_partidas.find():
    teams_partidas.append(match)

for jogo in teams_partidas:
    jogo['team_1'] = str(jogo['team_1']).replace('\n', '')
    jogo['team_2'] = str(jogo['team_2']).replace('\n', '')
    jogo['team_victory'] = str(
        jogo['team_victory']).replace('\n', '')
    jogo['team_defeat'] = str(
        jogo['team_defeat']).replace('\n', '')

cards = []
mapas = []

for jogo in teams_partidas:

    mapas = jogo['partida']

    n = 0
    for mapa in mapas:
        card1 = {}
        card2 = {}

        resultado_team_1 = mapa['placar'].split(' ')[0]
        resultado_team_2 = mapa['placar'].split(' ')[2]

        card1['team'] = jogo['team_1']
        card1['match'] = jogo['team_1'] + " X " + jogo['team_2']
        card1['map'] = mapa['Mapa']

        card2['team'] = jogo['team_2']
        card2['match'] = jogo['team_1'] + " X " + jogo['team_2']
        card2['map'] = mapa['Mapa']

        if jogo['team_1'] == jogo['team_victory']:
            card1['match_win'] = 1
            card2['match_win'] = 0
        else:
            card1['match_win'] = 0
            card2['match_win'] = 1

        if int(resultado_team_1) > int(resultado_team_2):
            card1['map_win'] = 1
            card2['map_win'] = 0
        else:
            card1['map_win'] = 0
            card2['map_win'] = 1

        card1['mapscore'] = int(resultado_team_1)
        card2['mapscore'] = int(resultado_team_2)

        card1['team_rating'] = str(mapa['team_rating']).split(' ')[0]
        card1['first_kills'] = int(str(mapa['first_kills']).split(' ')[0])
        card1['clutches_won'] = int(str(
            mapa['clutches_won']).split(' ')[0])
        cards.append(card1)

        card2['team_rating'] = str(mapa['team_rating']).split(' ')[2]
        card2['first_kills'] = int(str(mapa['first_kills']).split(' ')[2])
        card2['clutches_won'] = int(str(
            mapa['clutches_won']).split(' ')[2])
        cards.append(card2)

        n = n+1

dataset_iem_rio.insert_many(cards)

# Usando o pandas para montar uma tabela visualizavel
tabela = pd.DataFrame(list(cards))
with open("saida_texto.txt", "w", encoding="utf-8") as arquivo:
    arquivo.write(str(tabela))
