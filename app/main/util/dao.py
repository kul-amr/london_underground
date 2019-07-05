from flask_restplus import Namespace, fields


class StationDao:

    api = Namespace('Station', description='station related operations')
    station = api.model('Station', {
        'name': fields.String(required=True, description='name'),
        'total_lines': fields.Integer(required=True, description='total_lines'),
        'zone': fields.Integer(required=True, description='zone')
    })



class LineDao:

    api = Namespace('Line', description='line related operations')
    line = api.model('Line', {
        'name': fields.String(required=True, description='name'),
        'colour': fields.String(required=True, description='colour')
    })


class RouteDao:

    api = Namespace('Route', description='route related operations')
    route = api.model('Route', {
        'station':fields.String(required=True, description='station_name'),
        'time':fields.Integer(required=True, description='time_to_reach')
    })