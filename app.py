from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from decouple import config

from models.db import db
from routes.carreras import carreras

app = Flask(__name__)

app.secret_key = config("SECRET_KEY")
PGSQL_USER = config("PGSQL_USER")
PGSQL_PASSWORD = config("PGSQL_PASSWORD")
PGSQL_HOST = config("PGSQL_HOST")
PGSQL_PORT = config("PGSQL_PORT")
PGSQL_DATABASE = config("PGSQL_DATABASE")

DATABASE_CONNECTION_URI = f"postgresql://{PGSQL_USER}:{PGSQL_PASSWORD}@{PGSQL_HOST}:{PGSQL_PORT}/{PGSQL_DATABASE}"
app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_CONNECTION_URI
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
SQLAlchemy(app)
with app.app_context():
    db.create_all()
# db.init_app(app)

@app.route("/")
def index():
    return render_template("index.html")

def pagina_no_encontrada(error):
    return "<h1>Pagina no encontrada</h1>", 404

if __name__ == "__main__":
    app.register_blueprint(carreras, url_prefix="/carreras")
    app.register_error_handler(404, pagina_no_encontrada)
    # desarrollo
    app.run(debug=True, port=5000)
    # produccion
    # app.run()