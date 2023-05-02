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

    def iem_rio(db):
        iem_rio = db.iem_rio
        return iem_rio
