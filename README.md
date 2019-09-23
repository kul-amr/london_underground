# london_underground

Loaded the list of stations, lines and connections for London_Underground from the CSV datasets.
Built a representation of the stations and the connections between them.

Can use this model to answer some queries like Which station has the most interchanges? Or list of stations on a line? Or route-planning? For instance,
fastest route from Farringdon to Wembley?

Added some REST API endpoints, so a caller can make queries like:

GET /station/{station-id}
GET /station/{station-name}
GET /station/{station-name}/interchanges
GET /line/{line-name}/list-stations
GET /route/{start-station-name}/{destination-station-name}


Can deploy this code by followig steps :

1. Install the dependencies in virtual environment by

    pip install -r requirements.txt

2. Need to install neo4j graph database and create an environment variable "UNDERGROUND_NEO4J_PASS" to store password for default user "neo4j". Create a local database which will hold the data.

3. Load data into your local neo4j graph database by executing script load_data.py

    python load_data.py

3. Run the application

    python app.py


Now the API endpoints will be accessible locally.
