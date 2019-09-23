from flask import request
from flask_restplus import Resource
from flask_restplus import fields

from ..util.dao import RouteDao
from ..service.route_service import *

api = RouteDao.api
_route = RouteDao.route


@api.route('/<string:start_station_name>/<string:destination_station_name>')
@api.param('destination_station_name')
@api.param('start_station_name')
@api.response(404,'route not found')
class Route(Resource):
    @api.doc(params={'start_station_name': 'Start station of journey','destination_station_name':'Destination station of journey'})
    @api.response(200, 'OK')
    def get(self,start_station_name,destination_station_name):
        """
        Returns fastest route between stations
        """
        return get_route(start_station_name,destination_station_name)


@api.route('/<string:start_station_name>/<string:destination_station_name>/time')
@api.param('destination_station_name')
@api.param('start_station_name')
@api.response(404,'route not found')
class Route(Resource):
    @api.doc(params={'start_station_name': 'Start station of journey','destination_station_name':'Destination station of journey'})
    @api.marshal_list_with(_route)
    def get(self,start_station_name,destination_station_name):
        """
        Returns fastest route between stations with time
        """
        return get_route_with_time(start_station_name,destination_station_name)

