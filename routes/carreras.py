from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify

from models.db import db
from models.carreras import Carreras

carreras = Blueprint("carreras", __name__)

@carreras.route("/create", methods=["POST"])
def create():
    try:
        new = Carreras(request.form["carrera"])
        db.session.add(new)
        db.session.commit()
        flash("Creado con exito =)")
        return redirect(url_for("carreras.read"))
    except Exception as ex:
        return jsonify({"message": str(ex)}), 500

@carreras.route('/')
def read():
    try:
        return render_template("carrerasRead.html", object_list=Carreras.query.all())
    except Exception as ex:
        return jsonify({"message": str(ex)}), 500

@carreras.route("/update/<int:id>", methods=["GET", "POST"])
def update(id):
    try:
        carrera = Carreras.query.get(id)
        if request.method == "POST":
            carrera.carrera = request.form["carrera"]
            db.session.commit()
            flash("Actualizado con exito =)")
            return redirect(url_for("carreras.read"))
        return render_template("carrerasUpdate.html", object=carrera)
    except Exception as ex:
        return jsonify({"message": str(ex)}), 500

@carreras.route("/delete/<int:id>")
def delete(id):
    try:
        db.session.delete(Carreras.query.get(id))
        db.session.commit()
        flash("Eliminado con exito =)")
        return redirect(url_for("carreras.read"))
    except Exception as ex:
        return jsonify({"message": str(ex)}), 500