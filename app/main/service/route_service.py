from ..util.connect_db import *
from ..util.serializer import *


def get_route_with_time(start_station_name,destination_station_name):

    route_qry = 'MATCH (start:Station{{name:"{}"}}),(end:Station{{name:"{}"}}) ' \
                'CALL algo.shortestPath.stream(start, end, "time", {{nodeQuery: "Station"}}) ' \
                'YIELD nodeId, cost ' \
                'RETURN algo.getNodeById(nodeId).name as station, cost as time'.format(start_station_name,destination_station_name)

    result_route = execute_qry(route_qry)

    route_stations = []

    for record in result_route:
        station_stop = {}

        station_stop['station'] = record.get('station')
        station_stop['time'] = record.get('time')

        route_stations.append(station_stop)

    return [serialize_stop(station_stop) for station_stop in route_stations], 200


def get_route(start_station_name,destination_station_name):

    route_qry = 'MATCH (start:Station{{name:"{}"}}),(end:Station{{name:"{}"}}), ' \
                'p= shortestPath((start)-[:`Bakerloo Line`|`Northern Line`|`Central Line`|`Victoria Line`|`Jubilee Line`|' \
                '`Circle Line`|`District Line`|`Docklands Light Railway`|`East London Line`|`Hammersmith & City Line`|' \
                '`Metropolitan Line`|`Piccadilly Line`|`Waterloo & City Line`*]-(end)) RETURN p'.format(start_station_name,destination_station_name)

    result_route = execute_qry(route_qry)

    result = []

    for record in result_route:
        record_path = record.get('p')

        if record_path is not None:

            nodes = record_path.nodes
            relationships = record_path.relationships

            for m,n in zip(nodes,nodes[1::]):
                start = serialize_station(m)
                end = serialize_station(n)
                route = {}

                rels = [rel for rel in relationships if (rel.start_node==m or rel.end_node==m) and (rel.start_node==n or rel.end_node==n) ]

                route['line'] = rels[0].type
                route['time'] = rels[0].get('time')

                result.append({'start' : start,
                                'via': route,
                                'end' : end})

    return result, 200

