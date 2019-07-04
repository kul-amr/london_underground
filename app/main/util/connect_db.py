
from neo4j import GraphDatabase, basic_auth



driver = GraphDatabase.driver('bolt://localhost', auth=basic_auth("neo4j", "graph"))


def get_session():

    session = driver.session()

    return session