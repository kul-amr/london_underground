from ..util.connect_db import *
from ..util.serializer import *


def get_lines():

    lines_qry = "MATCH (n:Line) RETURN n"

    liness_resultset = execute_qry(lines_qry)

    print(liness_resultset)

    return [serialize_line(line.get('n')) for line in liness_resultset], 200


def add_line(data):

    merge_qry = '''MERGE (n:Line{{name: "{}"}}) 
                       ON CREATE SET n.colour = "{}"
                       ON MATCH SET n.colour = "{}"
                       RETURN n'''.format(data['name'], data['colour'], data['colour'])

    lines_resultset = execute_qry(merge_qry)

    for record in lines_resultset:
        return serialize_line(record.get('n')), 201

    return {'message': 'error in adding line'}, 404


def get_line(line_id=None, line_name=None):

    line_qry = ""

    if line_id is not None:
        line_qry = 'MATCH (n:Line) WHERE n.id="{}"  RETURN n LIMIT 1'.format(line_id)

    elif line_name is not None:
        line_qry = 'MATCH (n:Line) WHERE n.name="{}"  RETURN n LIMIT 1'.format(line_name)

    if len(line_qry) > 0:

        lines_resultset = execute_qry(line_qry)

        for record in lines_resultset:
            return serialize_line(record.get('n')), 200

    return {'message': 'line not found'}, 404


def get_stations(line_name):

    stations_qry = 'MATCH (p:Station)-[r:`{}`]->() ' \
                   'WITH distinct(p) RETURN p'.format(line_name)

    stations_resultset = execute_qry(stations_qry)

    return [serialize_station(station.get('p')) for station in stations_resultset], 200


def delete_line(line_name):

    del_qry = 'MATCH (n:Line) WHERE n.name="{}"  DELETE n RETURN COUNT(n) as deleted'.format(line_name)

    res = execute_qry(del_qry)

    for record in res:
        if record.get('deleted') > 0:
            return {'message': 'Line successfully deleted'}, 204

    return {'message':'Line not found'}, 404

