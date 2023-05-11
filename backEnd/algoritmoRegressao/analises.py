from banco import Banco

from pymongo import MongoClient
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
import seaborn as sns

# Organizar os dados para colocar no dataset
# Separar os dados por time
# Fazer uma tabela em que cada time vai ter varios rounds e em cada um desses rounds vai conter as informações se ganhou ou perdeu, o team rating, o first kill e o clutches won
# caracteristicas dos dados
# ganhou ou perdeu será binario
# team rating é a diferença entre kill e death do time todo
# o first kill serão as primeiras kills do jogo, essas kills representam uma vantagem na jogo
# o clutches won são rodadas na qual o time ganhou matando todos os outros do outro time

# Pegar os dados
banco_de_dados = Banco.inicia_banco()

# Acessa a Collection que guarda as informações para o dataset especifico

dataset_iem_rio = Banco.dataset_iem_rio(banco_de_dados)

# Guarda todos os dados da Collection em uma lista
matches = []
for match in dataset_iem_rio.find():
    matches.append(match)

dados = pd.DataFrame(list(matches))
dados = dados.drop('mapscore', axis=1)
dados = dados.drop('map_win', axis=1)

ax = sns.pairplot(dados, y_vars='match_win', x_vars=[
                  'team_rating', 'first_kills', 'clutches_won'])
plt.show()

with open("saida_texto2.txt", "w", encoding="utf-8") as arquivo:
    arquivo.write(str(ax))

print()

print(dados.describe().round(2))


dados = dados.drop('_id', axis=1)
dados = dados.drop('team', axis=1)
dados = dados.drop('match', axis=1)
dados = dados.drop('map', axis=1)

print(dados.corr().round(4))
