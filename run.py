from flask import Flask
import os
from app import blueprint
from app.main.util.ShortestPath import *


app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])

app.register_blueprint(blueprint)



@app.after_request
def after_request(response):
    print("in after_request")
    header = response.headers
    header['Access-Control-Allow-Origin'] = '*'
    print(response)
    return response

@app.route('/<name>')
def hello_name(name):

    get_dist()

    return "hello {} !".format(name)



app.run()

