from flask_restplus import Api
from flask import Blueprint

from .main.controller.station_controller import api as station_namespace
from .main.controller.line_controller import api as line_namespace


blueprint = Blueprint('api',__name__)

api = Api(blueprint,
          title='London underground api',
          version='1.0',
          description='London underground api description')


api.add_namespace(station_namespace,path='/stations')
api.add_namespace(line_namespace,path='/lines')
