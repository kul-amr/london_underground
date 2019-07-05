from flask import request
from flask_restplus import Resource
from flask_restplus import fields

from ..util.dao import RouteDao
from ..service.route_service import *

api = RouteDao.api
_route = RouteDao.route




@api.route('/<string:start_station_name>/<string:destination_station_name>')
@api.param('start_station_name','destination_station_name')
@api.response(404,'route not found')
class Route(Resource):
    @api.doc('get_route_between_stations')
    @api.marshal_list_with(_route)
    def get(self,start_station_name,destination_station_name):
        return get_route(start_station_name,destination_station_name)
