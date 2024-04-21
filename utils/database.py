from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv
import os

def dBConnection():
    # Load environment variables from .env file
    load_dotenv()

    # Fetch MongoDB URI from environment variables
    mongo_uri = os.getenv("MONGO_URI")

    # Create a new client and connect to the server
    client = MongoClient(mongo_uri, server_api=ServerApi('1'))

    # Fetch database and collection names from environment variables
    db_name = os.getenv("DB_NAME")
    collection_name = os.getenv("COLLECTION_NAME")

    # Create database and collection
    db = client[db_name]
    collection = db[collection_name]

    # Send a ping to confirm a successful connection
    try:
        client.admin.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB!")
        print("Connected to database:", db_name)
        print("Collection names:", db.list_collection_names())
    except Exception as e:
        print("Failed to connect to MongoDB:", e)

    return client, db, collection
