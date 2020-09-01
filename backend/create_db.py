from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from session.generator import UsersGenerator


def create_db(app: Flask, db: SQLAlchemy):

    app.app_context().push()
    db.create_all()

    generators = [
        UsersGenerator,
    ]

    max_initial_table_length = 20000

    for gen in generators:
        for idx, row in enumerate(gen):
            if(idx > max_initial_table_length):
                break
            db.session.add(row)

    db.session.commit()
