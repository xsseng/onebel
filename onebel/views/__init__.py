from flask import Blueprint
api = Blueprint('api', __name__, url_prefix='/api', template_folder='../templates', static_folder='../static')
users = Blueprint('admin', __name__, url_prefix='/admin', template_folder='../templates', static_folder='../static')
from . import action
from . import admin