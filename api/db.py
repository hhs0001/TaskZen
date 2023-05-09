from pymongo import MongoClient

tasks_collection = None

def connect_to_db(uri):
    global tasks_collection
    client = MongoClient(uri)
    db = client['taskzen']
    tasks_collection = db['tasks']

