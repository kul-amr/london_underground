from flask import request
from flask_restplus import Resource
from flask_restplus import fields

from ..util.dao import StationDao
from ..service.station_service import *

api = StationDao.api
_station = StationDao.station




@api.route('/')
class StationList(Resource):
    @api.doc('list_of_all_stations')
    @api.marshal_list_with(_station,envelope='data')
    def get(self):
        return get_stations()

    @api.response(201,'station created successfully')
    @api.doc('create_new_station')
    @api.expect(_station,validate=True)
    def post(self):
        data =  request.json
        return add_station(data)


@api.route('/<int:station_id>')
@api.param('station_id')
@api.response(404,'station not found')
class Station(Resource):
    @api.doc('get_station_with_id')
    @api.marshal_with(_station)
    def get(self, station_id):
        station = get_station(station_id=station_id)

        if not station:
            api.abort(404)
        else:
            return station


@api.route('/<string:station_name>')
@api.param('station_name')
@api.response(404,'station not found')
class Station(Resource):
    @api.doc('get_station_with_name')
    @api.marshal_with(_station)
    def get(self, station_name):
        station = get_station(station_name=station_name)

        if not station:
            api.abort(404)
        else:
            return station


@api.route('/<string:station_name>/interchanges')
@api.param('station_name')
@api.response(404,'station not found')
class StationInterchanges(Resource):
    @api.doc('get_tootal_interchanges_for_given_station_with_name')
    # @api.marshal_with({"interchanges":fields.Integer})
    def get(self, station_name):
        interchanges = get_station_interchanges(station_name=station_name)

        if not interchanges:
            api.abort(404)
        else:
            return interchanges