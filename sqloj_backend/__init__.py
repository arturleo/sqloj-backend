from flask import Flask, Blueprint
from flask_restx import Api

from .login import api as login_api
from .student import api as student_api
from .teacher import api as teacher_api


def create_app():
    app = Flask(__name__)

    # initialize extensions

    # initialize modules
    api_blueprint = Blueprint('api', __name__, url_prefix='/api')
    api = Api(api_blueprint)
    app.register_blueprint(api_blueprint)
    api.add_namespace(login_api, path='/login')
    api.add_namespace(student_api, path='/student')
    api.add_namespace(teacher_api, path='/teacher')

    return app
