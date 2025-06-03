from flask_sqlalchemy import SQLAlchemy
from flask import Flask

db = SQLAlchemy()

def init_db(app: Flask):
    app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:zebobin@localhost:5432/postgres"
    # Substitua 'user', 'password', 'host', 'port', 'database_name' pelas suas credenciais do PostgreSQL.
    # Exemplo: "postgresql://postgres:mysecretpassword@localhost:5432/meubanco"
    db.init_app(app)
    with app.app_context():
        db.create_all()