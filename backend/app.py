from flask import Flask, Blueprint
from flask_restful import Api

# Patch PYTHONPATH
from sys import path
path.append(".")

from backend import config
from backend.db import db
from backend.create_db import create_db

from backend.session.view import UserRootAPI, UserAPI, LoginAPI

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = config.DB_URI  
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = config.SQLALCHEMY_TRACK_MODIFICATIONS

db.init_app(app=app)

blueprint = Blueprint('api', __name__)
api = Api(blueprint)

api.add_resource(LoginAPI, "/login")
api.add_resource(UserRootAPI, "/user")
api.add_resource(UserAPI, "/user/<string:id>")

app.register_blueprint(blueprint, url_prefix='/api')

if __name__ == '__main__':
    create_db(app, db)
    app.run(host="0.0.0.0", port=config.PORT, debug=True, use_reloader=True)