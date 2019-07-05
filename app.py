from flask import Flask
import os
from app import blueprint


app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])

app.register_blueprint(blueprint)

# print(os.environ['APP_SETTINGS'])


@app.route('/')
def hello():
    return "hello world!"


@app.route('/<name>')
def hello_name(name):
    return "hello {} !".format(name)




# if __name__ == '__main__':

app.run()
