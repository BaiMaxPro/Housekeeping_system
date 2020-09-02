from flask_restful import Resource, reqparse

from backend.session.model import User, Session
from backend.db import db

from backend.view_utils import error

class UserRootAPI(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("username")
    parser.add_argument("password")
    parser.add_argument("role")

    def get(self):
        users = User.query.all()
        resp = [user.json() for user in users]
        return resp

    def post(self):
        args = self.parser.parse_args()

        username = args["username"]
        password = args["password"]
        role = args["role"]

        if role == None:
            role = "customer"

        if username == None or password == None:
            return error("Request must contain username and password.", 400)
        
        if not User.username_available(username):
            return error(f"Username '{username}' has been taken.", 400)

        try:
            user = User.new_user(username, password, role)
            db.session.add(user)
            db.session.commit()
            return user.json(), 201

        except Exception as e:
            return error(str(e), 400)
        
class UserAPI(Resource):
    def get(self, id):
        try:
            user = User.get_by_id(id)
        except AttributeError as e:
            return error(e, 400)
        except ValueError as e:
            return error(e, 404)
        
        return user.json()

def authenticated(f):
    def wrapper(*args, **kwargs):
        parser = reqparse.RequestParser()
        parser.add_argument('session-id', location='headers')

        try: 
            req = kwargs["testing_request"]
        except KeyError:
            req = None

        parsed_args = parser.parse_args(req)

        sess_id = parsed_args["session-id"]
        
        if sess_id == None:
            return error("Not authorized", 401)

        try:
            sess = Session.get_by_id(sess_id)
        except ValueError:
            return error("Not authorized", 401)
        except Exception as e:
            return error(str(e), 400)

        kwargs["session"] = sess
        kwargs["user"] = sess.user
        kwargs["role"] = sess.user.role

        return f(*args, **kwargs)
        
    return wrapper

class LoginAPI(Resource):

    @authenticated
    def get(self, **kwargs):
        return kwargs["session"].json(), 200

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("username", required=True, location='headers', help="Username is required") 
        parser.add_argument("password", required=True, location='headers', help="Password is required")
        args = parser.parse_args()
        
        username = args["username"]
        password = args["password"]

        try:
            user = User.get_by_username(username)
            if not user.check_password(password):
                raise ValueError
        except ValueError:
            return error("Username and/or password is incorrect.", 401)
        
        sess = Session.new_session(username)
        db.session.add(sess)
        db.session.commit()

        return sess.json(), 200

    @authenticated
    def delete(self, **kwargs):
        sess = kwargs["session"]
        db.session.delete(sess)
        db.session.commit()
        return {}, 204