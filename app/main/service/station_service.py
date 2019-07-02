from ..util.connect_db import *

from neo4j import GraphDatabase, basic_auth

def get_stations():

    session = get_session()
    stations = session.run("MATCH (a:Station) RETURN a")
    session.close()

    return stations


def add_station(data):

    return None


def get_station(station_id=None,station_name=None):
    driver = GraphDatabase.driver('bolt://localhost', auth=basic_auth("neo4j", "graph"))
    session = driver.session()

    print("get station ")

    station_qry = 'MATCH (n:Station) WHERE n.id="{}"  RETURN n LIMIT 25'.format(station_id)

    print(station_qry)

    station = session.run(station_qry)

    print("query executed")

    print(station)

    return station