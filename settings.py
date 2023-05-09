import configparser
import os
from api.db import get_tasks_collection

config = configparser.ConfigParser()
config.read(os.path.abspath(os.path.join(".ini")))

MONGO_URI = config['PROD']['DB_URI']
tasks_collection = get_tasks_collection(MONGO_URI)
