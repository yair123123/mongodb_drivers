from bson import ObjectId
from jinja2.lexer import Failure
from pymongo.errors import PyMongoError
from returns.result import Success

from database.connect import cars as default_cars


def insert_car(car: dict[str:str], collection=default_cars):
    try:
        car_id = collection.insert_one(car)
        return Success(car_id)
    except PyMongoError as e:
        return Failure(str(e))

def find_car_by_id(id: str, collection=default_cars):
    try:
        car = collection.find_one({"_id": ObjectId(id)})
        return Success(car)
    except PyMongoError as e:
        return Failure(str(e))

def find_all_cars(collection=default_cars):
    try:
        return Success(list(collection.find()))
    except PyMongoError as e:
        return Failure(str(e))


def update_car(id: str, to_update: dict[str:str], collection=default_cars):
     try:
        return Success(collection.update_one({"_id": ObjectId(id)}, {"$set":to_update}))
     except PyMongoError as e:
         return Failure(str(e))

def delete_car(id: str, collection=default_cars):
    try:
        return Success(collection.delete_one(find_car_by_id(id)))
    except PyMongoError as e:
        return Failure(str(e))