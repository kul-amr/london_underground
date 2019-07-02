from flask_restplus import Namespace, fields


class StationDao:

    api = Namespace('station', description='station related operations')
    station = api.model('station', {
        'name': fields.String(required=True, description='name'),
        'total_lines': fields.Integer(required=True, description='total_lines'),
        'zone': fields.Integer(required=True, description='zone')
    })