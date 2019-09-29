from flask import request
from flask_restplus import Resource
from flask_restplus import fields

from ..util.dao import StationDao, LineDao
from ..service.station_service import *

api = StationDao.api
_station = StationDao.station
_line = LineDao.line


@api.route('/')
class StationList(Resource):
    @api.doc('list_of_all_stations')
    @api.marshal_list_with(_station,envelope='data')
    def get(self):
        """
        Returns list of all stations
        """
        return get_stations()

    @api.response(201,'Station created successfully')
    @api.doc('create_new_station')
    @api.expect(_station,validate=True)
    def post(self):
        """
        Add a new station
        """
        data =  request.json
        return add_station(data)


@api.route('/<int:station_id>')
@api.param('station_id')
@api.response(404,'Station not found')
class Station(Resource):
    @api.doc(params={'station_id':'Id associated with the station'})
    @api.marshal_with(_station)
    def get(self, station_id):
        """
        Get station by Id
        """
        return get_station(station_id=station_id)


@api.route('/<string:station_name>')
@api.param('station_name')
@api.response(404,'Station not found')
class StationName(Resource):
    @api.doc(params={'station_name':'Name of the station'})
    @api.marshal_with(_station)
    def get(self, station_name):
        """
        Get station by name
        """
        return get_station(station_name=station_name)


    @api.response(204, 'Station successfully deleted')
    @api.doc(params={'station_name':'Name of the station'})
    def delete(self, station_name):
        """
        Delete station
        """
        return delete_station(station_name)


@api.route('/<string:station_name>/interchanges')
@api.param('station_name')
@api.response(404,'Station not found')
class StationInterchanges(Resource):
    @api.doc(params={'station_name':'Name of the station'})
    @api.response(200,'OK')
    def get(self, station_name):
        """
        Returns number of line interchanges available for given station
        """
        return get_station_interchanges(station_name=station_name)


@api.route('/<string:latitude>/<string:longitude>')
@api.param('longitude')
@api.param('latitude')
@api.response(404,'route not found')
class ClosestStation(Resource):
    @api.doc(params={'latitude':'latitude of location','longitude':'longitude of location'})
    @api.response(200, 'OK')
    def get(self,latitude,longitude):
        """
        Returns closest station to given co-ordinates, distance in meters
        """
        return get_closest_station(latitude,longitude)


@api.route('/<string:station_name>/connections')
@api.param('station_name')
@api.response(404,'station not found')
class StationConnections(Resource):
    @api.doc(params={'station_name':'Name of the station'})
    @api.response(200, 'OK')
    def get(self,station_name):
        """
        Returns direct connection stations to given station
        """
        return get_direct_connections(station_name)


@api.route('/<string:station_name>/lines')
@api.param('station_name')
@api.response(404,'station not found')
class StationLines(Resource):
    @api.doc(params={'station_name':'Name of the station'})
    @api.marshal_list_with(_line,envelope='data')
    def get(self,station_name):
        """
        Returns lines passing through the given station
        """
        return get_passing_lines(station_name)