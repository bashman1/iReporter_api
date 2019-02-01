from flask import Flask
from flask_jwt_extended import JWTManager

app = Flask(__name__)

app.config['JWT_SECRET_KEY'] = 'super-secret'
jwt = JWTManager(app)

from api.views import appblueprint

app.register_blueprint(views.appblueprint, url_prefix ='/v1/api/')
