from .db import db

class Especialidades(db.Model):
    id_especialidad = db.Column(db.Integer, primary_key=True)
    especialidad = db.Column(db.String(50), nullable=False)
    id_carrera = db.Column(db.Integer)

    def __init__(self, especialidad, id_carrera):
        self.especialidad = especialidad
        self.id_carrera = id_carrera