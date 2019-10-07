import sys


class Station:

    def __init__(self, station):

        self.name = station['name']
        self.total_lines = station['total_lines']
        self.zone = station['zone']
        self.lat = station['lat']
        self.lon = station['lon']

        self.adjacent_stations = {}
        self.visited = False
        self.previous = None
        self.distance = sys.maxsize

    def __lt__(self, other):
        return self.zone < other.zone

    def add_neighbour_station(self,neighbour_station, travel_time, connecting_line):

        route_dict ={}
        route_dict['line'] = connecting_line
        route_dict['time'] = travel_time
        self.adjacent_stations[neighbour_station] = route_dict

    def get_connections(self):

        return self.adjacent_stations.keys()

    def get_station(self):

        return self.name

    def get_travel_time(self,neighbour_station):

        return self.adjacent_stations[neighbour_station]['time']

    def set_distance(self,dist):

        self.distance = dist

    def get_distance(self):

        return self.distance

    def set_previous(self,prev):

        self.previous = prev

    def set_visited(self):

        self.visited = True

    def __str__(self):

        return self.name+ ' adjacent : '+ str([x.name for x in self.adjacent_stations])