import heapq
from ..models.Graph import Graph


def get_shortest(v,path):

    if v.previous:
        path.append(v.previous.get_station())
        get_shortest(v.previous,path)

    return


def dijkstra(graph,start,target):

    print("dijkstra shortest path")

    start.set_distance(0)

    unvisited_queue = [(v.get_distance(),v) for v in graph]
    heapq.heapify(unvisited_queue)

    while len(unvisited_queue):

        uv_elm = heapq.heappop(unvisited_queue)
        current_station = uv_elm[1]
        current_station.set_visited()

        for next_neighbour in current_station.adjacent_stations:

            if next_neighbour.visited:
                continue

            new_dist = current_station.get_distance() + current_station.get_travel_time(next_neighbour)

            if new_dist < next_neighbour.get_distance():
                next_neighbour.set_distance(new_dist)
                next_neighbour.set_previous(current_station)

                print("updated : current = {} , next = {}, new_dist = {} ".format(current_station,next_neighbour,next_neighbour.get_distance()))
            else:
                print("not updated : current = {} , next = {}, new_dist = {} ".format(current_station,next_neighbour,next_neighbour.get_distance()))


        while len(unvisited_queue):
            heapq.heappop(unvisited_queue)

        unvisited_queue = [(v.get_distance(),v) for v in graph if not v.visited]
        heapq.heapify(unvisited_queue)


def get_dist():

    g = Graph()

    baker_street = {'name':'Baker Street','total_lines':2,'zone':1,'lat':51,'lon':52}
    fin = {'name':'Finchley Road','total_lines':2,'zone':2,'lat':51,'lon':52}
    gp = {'name':'Great Portland Street','total_lines':2,'zone':1,'lat':51,'lon':52}
    rgp = {'name':'Regents Park','total_lines':2,'zone':1,'lat':51,'lon':52}
    mrb = {'name': 'Marylebone', 'total_lines': 2, 'zone': 1, 'lat': 51, 'lon': 52}
    jwd = {'name':"St. John's Wood",'total_lines':2,'zone':1,'lat':51,'lon':52}
    edwr = {'name':'Edgware Road (C)','total_lines':2,'zone':1,'lat':51,'lon':52}
    bond = {'name':'Bond Street','total_lines':2,'zone':1,'lat':51,'lon':52}
    oxford = {'name':'Oxford Circus','total_lines':3,'zone':1,'lat':51,'lon':52}



    g.add_station(baker_street)

    g.add_station(fin)
    g.add_station(gp)
    g.add_station(rgp)

    g.add_station(mrb)
    g.add_station(jwd)
    g.add_station(edwr)

    g.add_station(bond)


    g.add_travel_route(baker_street,fin,6,'Metropolitan Line')
    g.add_travel_route(baker_street,gp,3,'Hammersmith & City Line')
    g.add_travel_route(baker_street,rgp,2,'Bakerloo Line')

    g.add_travel_route(baker_street,mrb,1,'Bakerloo Line')
    g.add_travel_route(baker_street,jwd,4,'Jubilee Line')
    g.add_travel_route(baker_street,edwr,3,'Hammersmith & City Line')

    g.add_travel_route(baker_street,bond,2,'Jubilee Line')
    g.add_travel_route(baker_street,gp,3,'Circle Line')
    g.add_travel_route(baker_street,gp,3,'Metropolitan Line')

    g.add_travel_route(baker_street,edwr,3,'Circle Line')
    g.add_travel_route(bond,oxford,1,'Circle Line')
    g.add_travel_route(rgp,oxford,2,'Bakerloo Line')

    dijkstra(g,g.get_station('Baker Street'),g.get_station('Oxford Circus'))

    target = g.get_station('Oxford Circus')
    path = [target.get_station()]

    get_shortest(target,path)

    print("paths as : ")
    print(path)
    print("==================================================")
    print("the shortest path as : {}".format(path[::-1]))