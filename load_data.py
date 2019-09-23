from neo4j import GraphDatabase, basic_auth
import os


dir_path = os.path.dirname(os.path.realpath(__file__))
passwrd = os.environ.get("NEO4J_PASS")


def get_driver():

    driver = GraphDatabase.driver('bolt://localhost', auth=basic_auth("neo4j", passwrd))
    return driver


def create_schema():

    driver = get_driver()

    qry_constraint = "CREATE CONSTRAINT ON (s:Station) ASSERT s.id is unique;"
    qry_constraint_oth = "CREATE CONSTRAINT ON (s:Station) ASSERT s.name is unique;"

    with driver.session() as session:
        session.run(qry_constraint)
        session.run(qry_constraint_oth)
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


def create_lines_relations():

    driver = get_driver()

    qry_rel = '''LOAD CSV WITH HEADERS FROM
                            "file:///%s/datasets/london-connections.csv" as row
                            MATCH (s1:Station{id:row.station1}),(s2:Station{id:row.station2}),(l:Line)
                            WHERE l.id = row.line
                            CALL apoc.create.relationship(s1,l.name,{time:row.time,line:row.line},s2) YIELD rel
                            RETURN rel''' %dir_path

    with driver.session() as session:
        session.run(qry_rel)
    session.close()


def main():

    create_schema()

    import_lines()
    import_stations()
    import_connections()



main()


# MATCH (l:Line), ()-[r:CONNECTION]->() SET(CASE WHEN r.line=l.id THEN r END).line_name = l.name  RETURN r


# LOAD CSV WITH HEADERS FROM
#                             "file:///home/amruta/Amruta/london_underground/datasets/london-connections.csv" as row
#                             MATCH (s1:Station{id:row.station1}),(s2:Station{id:row.station2}),(l:Line)
#                             WHERE l.id = row.line
#                             CALL apoc.create.relationship(s1,l.name,{time:row.time,line:row.line},s2) YIELD rel
#                             RETURN rel


# MATCH (a)-[r:`Bakerloo Line`]->(b), (l:Line) WHERE l.id=r.line CREATE (a)-[p:ON_LINE]->(l) RETURN p

# MATCH (a)-[r:`Central Line`]->(b), (l:Line) WHERE l.id=r.line MERGE (a)-[p:ON_LINE]->(l) RETURN p
# MATCH (a)-[r:`East London Line`]->(b), (l:Line) WHERE l.id=r.line MERGE (a)-[p:ON_LINE]->(l) RETURN p
# MATCH (a)-[r:`District Line`]->(b), (l:Line) WHERE l.id=r.line MERGE (a)-[p:ON_LINE]->(l) RETURN p



# MATCH (a)-[r]->(b) SET r.time = toInt(r.time)
