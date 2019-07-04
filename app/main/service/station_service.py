from ..util.connect_db import *


def serialize_station(station):

    return {
        'name': station["name"],
        'total_lines': station["total_lines"],
        'zone': station["zone"]
    }


def get_stations():

    session = get_session()

    stations_resultset = session.run("MATCH (n:Station) RETURN n.name as name, n.total_lines as total_lines, n.zone as zone")

    session.close()

    return [serialize_station(station) for station in stations_resultset]


def add_station(data):

    merge_qry = '''MERGE (n:Station{{name: "{}"}}) 
                    ON CREATE SET n.total_lines = "{}", n.zone = "{}" 
                    ON MATCH SET n.total_lines = "{}", n.zone = "{}"
                    RETURN n.name as name, n.total_lines as total_lines, 
                    n.zone as zone'''.format(data['name'],data['total_lines'],data['zone'],data['total_lines'],data['zone'])

    session = get_session()

    stations_resultset = session.run(merge_qry)

    session.close()

    for record in stations_resultset:
        return serialize_station(record), 201

    return {'message':'error in adding station'}, 404


def get_station(station_id=None,station_name=None):

    session = get_session()

    station_qry=""

    if station_id is not None:
        station_qry = 'MATCH (n:Station) WHERE n.id="{}"  RETURN n.name as name, ' \
                      'n.total_lines as total_lines, n.zone as zone LIMIT 1'.format(station_id)

    elif station_name is not None:
        station_qry = 'MATCH (n:Station) WHERE n.name="{}"  RETURN n.name as name, ' \
                      'n.total_lines as total_lines, n.zone as zone LIMIT 1'.format(station_name)

    if len(station_qry) > 0:

        station = session.run(station_qry)

        session.close()

        for record in station:
            return serialize_station(record)

    return {'message':'station not found'}, 404


def get_station_interchanges(station_name):

    session = get_session()

    interchanges_qry = 'MATCH (n:Station) WHERE n.name="{}"  RETURN n.total_lines as interchanges'.format(station_name)

    station = session.run(interchanges_qry)

    session.close()

    for record in station:
        print(record["interchanges"])
        return {"interchanges": record["interchanges"]}

    return {'message': 'station not found'}, 404