from .db import db

class Calificaciones(db.Model):
    id_calificacion = db.Column(db.Integer, primary_key=True)
    calificacion = db.Column(db.Float, nullable=False)
    id_alumno = db.Column(db.Integer, nullable=False)
    id_materia = db.Column(db.Integer)

    def __init__(self, calificacion, id_alumno, id_materia):
        self.calificacion = calificacion
        self.id_alumno = id_alumno
        self.id_materia = id_materia