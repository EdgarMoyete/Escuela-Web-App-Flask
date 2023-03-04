from .db import db

class Alumnos(db.Model):
    id_alumno = db.Column(db.Integer, primary_key=True)
    apellido_paterno = db.Column(db.String(30), nullable=False)
    apellido_materno = db.Column(db.String(30))
    nombres = db.Column(db.String(30), nullable=False)
    sexo = db.Column(db.String(1))
    curp = db.Column(db.String(18))
    id_carrera = db.Column(db.Integer)
    id_especialidad = db.Column(db.Integer)

    def __init__(
        self, apellido_paterno, apellido_materno, nombres, sexo, curp, id_carrera, id_especialidad
    ):
        self.apellido_paterno = apellido_paterno
        self.apellido_materno = apellido_materno
        self.nombres = nombres
        self.sexo = sexo
        self.curp = curp
        self.id_carrera = id_carrera
        self.id_especialidad = id_especialidad