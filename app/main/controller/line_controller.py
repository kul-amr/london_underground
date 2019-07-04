from flask import request
from flask_restplus import Resource

from ..util.dao import LineDao
from ..service.line_service import *

api = LineDao.api
_line = LineDao.line




@api.route('/')
class LineList(Resource):
    @api.doc('list_of_all_lines')
    @api.marshal_list_with(_line,envelope='data')
    def get(self):
        return get_lines()

    @api.response(201,'line created successfully')
    @api.doc('create_new_line')
    @api.expect(_line,validate=True)
    def post(self):
        data =  request.json
        return add_line(data)


@api.route('/<int:line_id>')
@api.param('line_id')
@api.response(404,'line not found')
class Line(Resource):
    @api.doc('get_line_with_id')
    @api.marshal_with(_line)
    def get(self, line_id):
        line = get_line(line_id=line_id)

        if not line:
            api.abort(404)
        else:
            return line


@api.route('/<string:line_name>')
@api.param('line_name')
@api.response(404,'line not found')
class Line(Resource):
    @api.doc('get_line_with_name')
    @api.marshal_with(_line)
    def get(self, line_name):
        line = get_line(line_name=line_name)

        if not line:
            api.abort(404)
        else:
            return line
