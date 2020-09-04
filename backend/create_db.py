from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from backend.session.generator import UsersGenerator
from backend.customer.generator import CustomersGenerator

def create_db(app: Flask, db: SQLAlchemy):

    app.app_context().push()

    print("Creating tables...")
    db.create_all()

    generators = [
        UsersGenerator,
        CustomersGenerator,
    ]

    max_initial_table_length = 20000

    print("Populating tables...")
    for gen in generators:
        for idx, row in enumerate(gen):
            if(idx > max_initial_table_length):
                break
            db.session.add(row)
        db.session.commit()

