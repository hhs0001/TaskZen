import configparser
import os
from flask import Flask
from flask_cors import CORS
from api.db import connect_to_db
from api.tasks import tasks_blueprint

app = Flask(__name__)
CORS(app)

config = configparser.ConfigParser()
config.read(os.path.abspath(os.path.join(".ini")))

app.config['MONGO_URI'] = config['PROD']['DB_URI']

print(app.config['MONGO_URI'])

# Conexão com o MongoDB Atlas
MONGO_URI = app.config['MONGO_URI']
connect_to_db(MONGO_URI)

# Registra o blueprint do módulo tasks
app.register_blueprint(tasks_blueprint, url_prefix='/api')

if __name__ == '__main__':
    from os import environ
    from werkzeug.serving import run_simple

    if environ.get("WERKZEUG_RUN_MAIN") == "true":
        app.debug = True
    run_simple('localhost', 5000, app, use_debugger=True, use_reloader=True)
