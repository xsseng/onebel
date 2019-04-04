from flask import Blueprint
api = Blueprint('api', __name__, url_prefix='/api', template_folder='../templates', static_folder='../static')
main = Blueprint('main', __name__, url_prefix='/admin', template_folder='../templates', static_folder='../static')
from . import apis
from . import admin