from pymongo import MongoClient


class Banco:
    def inicia_banco():
        client = MongoClient(
            'mongodb+srv://gabrielhjalberto:Alberto60127842@cluster0.t8961c5.mongodb.net/test')
        db = client.Predict_win_rate
        return db

    def teams(db):
        teams = db.teams
        return teams

    def convertenome(nome):
        nome = nome.replace(',', '').replace('-', '').replace(' ', '').replace('(', '').replace(':', '').replace('|', '').replace('?', '').replace('{', '').replace('}', '').replace('`', '').replace('^', '').replace(')', '').replace(
            '.', '').replace('/', '').replace('"', '').replace('!', '').replace(';', '').replace('+', '').replace('~', '').replace('<', '').replace('>', '').replace('	', '').replace('*', '').replace('\'', '').lower()
        return nome