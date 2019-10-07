

def serialize_station(station):

    return {
        'name': station["name"],
        'total_lines': station["total_lines"],
        'zone': station["zone"],
        'latitude': station["latitude"],
        'longitude': station["longitude"]
    }


def serialize_line(line):

    return {
        # 'id':line["id"],
        'name': line["name"],
        'colour': line["colour"]
    }


def serialize_stop(station_stop):

    return {
        'station' : station_stop["station"],
        'time' : station_stop["time"]
    }


def serialize_closest_station(station,distance):

    closest_station = serialize_station(station)

    closest_station['distance'] = distance

    return closest_station


def serialize_relationship(relationship):

    nodes = relationship.nodes

    start = {}
    end = {}
    route = {}

    if len(nodes) >0:
        start = serialize_station(nodes[0])
        end = serialize_station(nodes[1])

    route['line'] = relationship.type
    route['time'] = relationship.get('time')

    return {
        'start' : start,
        'via': route,
        'end' : end
    }
