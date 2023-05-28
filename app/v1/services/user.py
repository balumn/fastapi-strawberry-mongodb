from app.core.schemas.user import User, user_to_dict, user_from_dict
from app.db import db


def get_all_users_from_mongo():
    users_collection = db["users"]  # Replace "users" with your actual collection name
    users = users_collection.find()
    return [user_from_dict(user) for user in users]


def insert_user_to_mongo(user: User):
    users_collection = db["users"]
    users_collection.insert_one(user_to_dict(user))

