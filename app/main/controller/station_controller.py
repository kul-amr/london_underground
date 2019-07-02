from flask import request
from flask_restplus import Resource

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


@api.route('/<station_id>')
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
