from pymongo import MongoClient


class Banco:
    def inicia_banco():
        client = MongoClient(
            'mongodb+srv://onorak:carlos123@cluster0.t8961c5.mongodb.net/test')
        db = client.Predict_win_rate
        return db

    def teams(db):
        teams = db.teams
        return teams

    def teams_details(db):
        teams_details = db.teams_details
        return teams_details

    def campeonatos(db):
        campeonatos = db.campeonatos
        return campeonatos

    def partidas(db):
        partidas = db.partidas
        return partidas

    def dataset_iem_rio(db):
        dataset_iem_rio = db.dataset_iem_rio
        return dataset_iem_rio
