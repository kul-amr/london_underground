
from neo4j import GraphDatabase, basic_auth


def get_session():

    driver = GraphDatabase.driver('bolt://localhost', auth=basic_auth("neo4j", "graph"))
    session = driver.session()

    return session