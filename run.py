from flask import Flask
import os
from app import blueprint
from flask_cors import CORS


app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])

app.register_blueprint(blueprint)


CORS(app)


@app.route('/<name>')
def hello_name(name):
    return "hello {} !".format(name)



app.run()

