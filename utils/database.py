from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv
import os

load_dotenv()

def databaseConnection():
    mongo_uri = os.getenv("MONGO_URI")

    client = MongoClient(mongo_uri, server_api=ServerApi('1'))

    db_name = os.getenv("DB_NAME")
    collection_name = os.getenv("COLLECTION_NAME")

    # Create database and collection
    db = client[db_name]
    collection = db[collection_name]

    try:
        client.admin.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB!")
        print("Connected to database:", db_name)
        print("Collection names:", db.list_collection_names())
        print("Collection is as:", collection_name)
    except Exception as e:
        print("Failed to connect to MongoDB:", e)

    return client, db, collection_name
