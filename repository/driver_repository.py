from bson import ObjectId
from pymongo.errors import PyMongoError
from returns.result import Success, Failure

from database.connect import drivers as drivers_default


def insert_driver(driver: dict[str:str], collection=drivers_default):
    try:
        driver_id = collection.insert_one(driver)
        return Success(driver_id)
    except PyMongoError as e:
        return Failure(str(e))


def find_driver_by_id(id: str, collection=drivers_default):
    try:
        driver = collection.find_one({"_id": ObjectId(id)})
        return driver
    except PyMongoError as e:
        return Failure(str(e))

def find_all_drivers(collection=drivers_default):
    try:
        return Success(list(collection.find()))
    except PyMongoError as e:
        return Failure(str(e))

def update_driver(id: str, driver_updated: dict[str:str], collection=drivers_default):
    try:
        return Success(collection.update_one({"_id": ObjectId(id)}, {"$set": driver_updated}))
    except PyMongoError as e:
        return Failure(str(e))

def delete_driver(id: str, collection=drivers_default):
    try:
        return Success(collection.delete_one(find_driver_by_id(id)))
    except PyMongoError as e:
        return Failure(str(e))