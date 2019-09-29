from ..util.connect_db import *
from ..util.serializer import *


def get_stations():

    stations_qry = "MATCH (n:Station) RETURN n"

    stations_resultset = execute_qry(stations_qry)

    return [serialize_station(station.get('n')) for station in stations_resultset], 200


def add_station(data):

    merge_qry = '''MERGE (n:Station{{name: "{}"}}) 
                    ON CREATE SET n.total_lines = {}, n.zone = {}, n.latitude = {}, n.longitude = {} 
                    ON MATCH SET n.total_lines = {}, n.zone = {}, n.latitude = {}, n.longitude = {}
                    RETURN n'''.format(data['name'],data['total_lines'],data['zone'],data['latitude'],data['longitude'],
                                                       data['total_lines'],data['zone'],data['latitude'],data['longitude'])

    stations_resultset = execute_qry(merge_qry)

    for record in stations_resultset:
        return serialize_station(record.get('n')), 201

    return {'message':'error in adding station'}, 404


def get_station(station_id=None,station_name=None):

    station_qry=""

    if station_id is not None:
        station_qry = 'MATCH (n:Station) WHERE n.id="{}"  RETURN n LIMIT 1'.format(station_id)

    elif station_name is not None:
        station_qry = 'MATCH (n:Station) WHERE n.name="{}"  RETURN n LIMIT 1'.format(station_name)

    print(station_qry)

    if len(station_qry) > 0:

        station = execute_qry(station_qry)

        for record in station:
            return serialize_station(record.get('n')), 200

    return {'message':'Station not found'}, 404


def delete_station(name):

    del_qry = 'MATCH (n:Station) WHERE n.name="{}" DELETE n RETURN COUNT(n) as deleted'.format(name)

    res = execute_qry(del_qry)

    for record in res:
        if record.get('deleted') > 0:
            return {'message': 'Station successfully deleted'}, 204

    return {'message':'Station not found'}, 404


def get_station_interchanges(station_name):

    interchanges_qry = 'MATCH (n:Station) WHERE n.name="{}"  RETURN n.total_lines as interchanges'.format(station_name)

    station = execute_qry(interchanges_qry)

    for record in station:
        return {"interchanges": record["interchanges"]}, 200

    return {'message': 'Station not found'}, 404


def get_closest_station(latitude,longitude):

    station_qry = 'MATCH (near:Station) ' \
                  'WITH near, point(near) AS start, point({{latitude: {}, longitude: {} }}) AS destination ' \
                  'WITH near, distance(start, destination) AS distance ' \
                  'RETURN near, distance ORDER BY distance ASC LIMIT 1 '.format(latitude,longitude)

    result_station = execute_qry(station_qry)

    for record in result_station:
        return serialize_closest_station(record['near'],round(record['distance'],2)), 200

    return {'message': 'station not found'}, 404


def get_direct_connections(station_name):

    connections_qry = 'MATCH path=(:Station{{name:"{}"}})-[]-(:Station) RETURN path'.format(station_name)

    result_stations = execute_qry(connections_qry)

    record_relationships = []

    for record in result_stations:
        record_relationship = record.get('path').relationships[0]
        record_relationships.append(record_relationship)

    return [serialize_relationship(rel) for rel in record_relationships], 200


def get_passing_lines(station_name):

    line_qry = 'MATCH (a:Station)-[r:ON_LINE]-(b) WHERE a.name="{}" RETURN b'.format(station_name)

    result_lines = execute_qry(line_qry)

    return [serialize_line(record.get('b')) for record in result_lines], 200
