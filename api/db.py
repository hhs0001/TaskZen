# api/db.py
from pymongo import MongoClient

def get_tasks_collection(mongo_uri):
    client = MongoClient(mongo_uri)
    db = client['taskzen']
    tasks_collection = db['tasks']
    return tasks_collection
