import os
from neo4j import GraphDatabase, basic_auth


passwrd = os.environ.get("UNDERGROUND_NEO4J_PASS")


driver = GraphDatabase.driver('bolt://localhost', auth=basic_auth("neo4j", passwrd))


def get_session():

    session = driver.session()

    return session