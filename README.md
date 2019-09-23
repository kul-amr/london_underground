# london_underground

I had worked with relational and no-sql data in past but not the graph data. I wanted to learn/explore about how to use/serve graph data.
So I started to exlpore a bit about Neo4j graph database and Cypher query language.

Here I have created a backend with Python (flask-restplus) querying Neo4j garph database with Cypher queries. I have used london undergrounds
data CSVs of list of stations,lines and connections between various stations.

Loaded the list of stations, lines and connections for London_Underground from the CSV datasets.
Built a representation of the stations and the connections between them.

Can use this model to answer some queries like which station has the most interchanges? Or direct connections for a station?
Or list of stations on a line? Or closest station to given latitude, longitude? Or route-planning? For instance, fastest route from Farringdon to Wembley?

Added some REST API endpoints, so a caller can make queries like:

GET /station/{station-id}
GET /station/{station-name}
GET /station/{station-name}/interchanges
GET /line/{line-name}/stations
GET /route/{start-station-name}/{destination-station-name}

(Screenshots at the bottom of the page)

Can deploy this code by followig steps :

1. Install the dependencies in virtual environment by

    pip install -r requirements.txt

2. Need to install neo4j graph database and create an environment variable "NEO4J_PASS" to store password
   for default user "neo4j". Create a local database which will hold the data.
   (for now, here I am using Neo4j Graph Algorithm library for path finding, distance and connections queries. The plugins for
   this library can be installed as https://neo4j.com/docs/graph-algorithms/current/introduction/#_installation)

3. Load data into your local neo4j graph database by executing script load_data.py

    python load_data.py

3. Run the application

    python run.py


Now the API endpoints will be accessible locally.

![Alt text](/screen_shots/screen1.png)
![Alt text](/screen_shots/screen2.png)
![Alt text](/screen_shots/screen3.png)
![Alt text](/screen_shots/screen4.png)
![Alt text](/screen_shots/screen5.png)
![Alt text](/screen_shots/screen6.png)