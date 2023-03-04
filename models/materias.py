from .db import db

class Materias(db.Model):
    id_materia = db.Column(db.Integer, primary_key=True)
    materia = db.Column(db.String(50), nullable=False)
    id_carrera = db.Column(db.Integer)

    def __init__(self, materia, id_carrera):
        self.materia = materia
        self.id_carrera = id_carrera