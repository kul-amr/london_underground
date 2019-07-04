from ..util.connect_db import *


def serialize_line(line):

    return {
        'name': line["name"],
        'colour': line["colour"]
    }


def get_lines():

    session = get_session()

    liness_resultset = session.run(
        "MATCH (n:Line) RETURN n.name as name, n.colour as colour")

    session.close()

    return [serialize_line(line) for line in liness_resultset]


def add_line(data):

    merge_qry = '''MERGE (n:Line{{name: "{}"}}) 
                       ON CREATE SET n.colour = "{}"
                       ON MATCH SET n.colour = "{}"
                       RETURN n.name as name, n.colour as colour'''.format(data['name'], data['colour'], data['colour'])

    session = get_session()

    lines_resultset = session.run(merge_qry)

    session.close()

    for record in lines_resultset:
        return serialize_line(record), 201

    return {'message': 'error in adding line'}, 404


def get_line(line_id=None, line_name=None):

    session = get_session()

    line_qry = ""

    if line_id is not None:
        line_qry = 'MATCH (n:Line) WHERE n.id="{}"  RETURN n.name as name, ' \
                      'n.colour as colour LIMIT 1'.format(line_id)

    elif line_name is not None:
        line_qry = 'MATCH (n:Line) WHERE n.name="{}"  RETURN n.name as name, ' \
                      'n.colour as colour LIMIT 1'.format(line_name)

    if len(line_qry) > 0:

        lines_resultset = session.run(line_qry)

        session.close()

        for record in lines_resultset:
            return serialize_line(record)

    return {'message': 'line not found'}, 404