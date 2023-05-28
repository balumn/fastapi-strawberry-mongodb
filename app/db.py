from os import getenv

from pymongo import MongoClient


# get mongodb URI and database name from environment variable
MONGO_URI = "mongodb://{}:{}@{}:{}/?retryWrites=true&serverSelectionTimeoutMS=5000&connectTimeoutMS=10000&authSource=admin&authMechanism=SCRAM-SHA-256".format(
    getenv("MONGO_USERNAME", default="root"),
    getenv("MONGO_PASSWORD", default="example"),
    getenv("MONGO_HOST", default="127.0.0.1"),
    getenv("MONGO_PORT", default="27017")
)
MONGO_DATABASE = getenv("MONGO_DATABASE", default="dobby_travels")

# instantiate mongo client
client = MongoClient(MONGO_URI, serverSelectionTimeoutMS=2000)

# get database
db = client[MONGO_DATABASE]
