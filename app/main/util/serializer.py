

def serialize_station(station):

    return {
        'name': station["name"],
        'total_lines': station["total_lines"],
        'zone': station["zone"]
    }


def serialize_line(line):

    return {
        'name': line["name"],
        'colour': line["colour"]
    }

def serialize_stop(station_stop):

    return {
        'station' : station_stop["station"],
        'time' : station_stop["time"]
    }
