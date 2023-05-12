# api/db.py
from pymongo import MongoClient

def get_db_collections(mongo_uri):
    client = MongoClient(mongo_uri)
    db = client['taskzen']
    tasks_collection = db['tasks']
    users_collection = db['users']
    return tasks_collection, users_collection
