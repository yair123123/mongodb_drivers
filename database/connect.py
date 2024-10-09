from pymongo import MongoClient


client = MongoClient('mongodb://172.29.168.75:27017')
taxi_db = client['taxi-drivers']


drivers = taxi_db['drivers']
cars = taxi_db['cars']