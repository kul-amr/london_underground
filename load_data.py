from neo4j import GraphDatabase, basic_auth
import os


dir_path = os.path.dirname(os.path.realpath(__file__))


def get_driver():

    driver = GraphDatabase.driver('bolt://localhost', auth=basic_auth("neo4j", "graph"))
    return driver

def create_schema():

    driver = get_driver()

    qry_constraint = "CREATE CONSTRAINT ON (s:Station) ASSERT s.id is unique;"
    qry_constraint_oth = "CREATE CONSTRAINT ON (s:Station) ASSERT s.name is unique;"
    # qry_index = "CREATE INDEX ON :Station(name);"

    with driver.session() as session:
        session.run(qry_constraint)
        session.run(qry_constraint_oth)
        # session.run(qry_index)
    session.close()


def import_stations():
    driver = get_driver()

    qry_stations = 'LOAD CSV WITH HEADERS FROM ' \
                   ' "file:///%s/datasets/london-stations.csv" as row' \
                   ' MERGE (s:Station{id:row.id}) ' \
                   'ON CREATE SET s.name = row.name,' \
                   's.latitude=row.latitude,' \
                   ' s.longitude=row.longitude,' \
                   's.zone=row.zone,' \
                   ' s.total_lines=row.total_lines' %dir_path


    with driver.session() as session:
        session.run(qry_stations)
    session.close()

def import_lines():
    driver = get_driver()

    qry_lines = '''LOAD CSV WITH HEADERS FROM
                           "file:///%s/datasets/london-lines.csv" as row
                       MERGE (l:Line{id:row.line})
                       ON CREATE SET l.name = row.name,
                         l.colour=row.colour,
                         l.stripe=row.stripe''' %dir_path


    with driver.session() as session:
        session.run(qry_lines)
    session.close()

def import_connections():

    driver = get_driver()

    qry_connections = '''LOAD CSV WITH HEADERS FROM
                            "file:///%s/datasets/london-connections.csv" as row
                            MATCH (s1:Station{id:row.station1})
                            MATCH (s2:Station{id:row.station2})
                            MERGE (s1)-[:CONNECTION{time:row.time,line:row.line}]->(s2)
                            MERGE (s1)<-[:CONNECTION{time:row.time,line:row.line}]-(s2)''' %dir_path


    with driver.session() as session:
        session.run(qry_connections)
    session.close()


def main():

    create_schema()

    import_lines()
    import_stations()
    import_connections()



main()