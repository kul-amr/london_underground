

def serialize_station(station):

    print(station)
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

