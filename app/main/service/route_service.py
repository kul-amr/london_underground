from ..util.connect_db import *
from ..util.serializer import *


def get_route(start_station_name,destination_station_name):

    print(start_station_name, destination_station_name)
    session = get_session()

    route_qry = 'MATCH (start:Station{{name:"{}"}}),(end:Station{{name:"{}"}}) ' \
                'CALL algo.shortestPath.stream(start, end, "time") ' \
                'YIELD nodeId, cost MATCH (s:Station) ' \
                'where id(s)=nodeId ' \
                'RETURN s.name as station,cost as time'.format(start_station_name,destination_station_name)

    print(route_qry)

    result_route = session.run(route_qry)

    print(result_route)

    return [serialize_stop(station_stop) for station_stop in result_route]


