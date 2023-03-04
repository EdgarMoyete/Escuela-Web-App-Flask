from .db import db

class Carreras(db.Model):
    id_carrera = db.Column(db.Integer, primary_key=True)
    carrera = db.Column(db.String(50), nullable=False)

    def __init__(self, carrera):
        self.carrera = carrera