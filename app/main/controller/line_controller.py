from flask import request
from flask_restplus import Resource, cors

from ..util.dao import LineDao, StationDao
from ..service.line_service import *

api = LineDao.api
_line = LineDao.line
_station = StationDao.station


@api.route('/')
class LineList(Resource):
    @api.doc('list_of_all_lines')
    @api.marshal_list_with(_line,envelope='data')
    # @cors.crossdomain(origin='*')
    def get(self):
        """
        Get list of all lines
        """
        print("caling lines ")
        return get_lines()

    @api.response(201,'line successfully created')
    @api.doc('create_new_line')
    @api.expect(_line,validate=True)
    def post(self):
        """
        Add a new line
        """
        data =  request.json
        return add_line(data)


@api.route('/<int:line_id>')
@api.param('line_id')
@api.response(404,'line not found')
class Line(Resource):
    @api.doc(params={'line_id': 'Id associated with the line'})
    @api.marshal_with(_line)
    def get(self, line_id):
        """
        Get line by Id
        """
        return get_line(line_id=line_id)


@api.route('/<string:line_name>')
@api.param('line_name')
@api.response(404,'line not found')
class LineName(Resource):
    @api.doc(params={'line_name': 'Name of the line'})
    @api.marshal_with(_line)
    def get(self, line_name):
        """
        Get line by name
        """
        return get_line(line_name=line_name)

    @api.response(204, 'line successfully deleted')
    @api.doc(params={'line_name': 'Name of the line'})
    def delete(self, line_name):
        """
        Delete line
        """
        return delete_line(line_name)


@api.route('/<string:line_name>/stations')
@api.param('line_name')
@api.response(404,'line not found')
class LineStations(Resource):
    @api.doc(params={'line_name': 'Name of the line'})
    @api.marshal_list_with(_station,envelope='data')
    def get(self, line_name):
        """
        Get all stations which are on given line
        """
        return get_stations(line_name=line_name)