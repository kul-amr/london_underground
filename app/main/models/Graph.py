from .Station import Station


class Graph:

    def __init__(self):

        self.stations_dict = {}
        self.stations_count = 0

    def __iter__(self):

        return iter(self.stations_dict.values())

    def add_station(self,station):

        self.stations_count = self.stations_count+1
        new_station = Station(station)
        self.stations_dict[station['name']] = new_station
        return new_station

    def get_station(self,stationName):

        if stationName in self.stations_dict:
            return self.stations_dict[stationName]
        else:
            return None

    def add_travel_route(self, from_station,to_station, travel_time, line_name):

        if from_station['name'] not in self.stations_dict:
            self.add_station(from_station)

        if to_station['name'] not in self.stations_dict:
            self.add_station(to_station)

        self.stations_dict[from_station['name']].add_neighbour_station(self.stations_dict[to_station['name']],travel_time, line_name)
        self.stations_dict[to_station['name']].add_neighbour_station(self.stations_dict[from_station['name']],travel_time, line_name)

    def get_stations(self):

        return self.stations_dict.keys()


