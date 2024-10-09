from database.connect import drivers, cars
from utils.csv_util import read_csv



def init_taxi_drivers():
    drivers.drop()
    cars.drop()

    for row in read_csv("practice_data.csv"):
        car = {
            'license_id': row['CarLicense'],
            'brand': row['CarBrand'],
            'color': row['CarColor']
        }

        car_id = cars.insert_one(car).inserted_id

        address = {
            'city': row['City'],
            'street': row['Street'],
            'state': row['State']
        }

        driver = {
            'passport': row['PassportNumber'],
            'first_name': row['FullName'].split(' ')[0],
            'last_name': row['FullName'].split(' ')[1],
            'car_id': car_id,
            'address': address
        }
        drivers.insert_one(driver)
