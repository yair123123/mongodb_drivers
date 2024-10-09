import pytest
from pymongo.collection import Collection




@pytest.fixture(scope="function")
def cars_collection(init_test_data):
   return init_test_data['cars']


def test_find_all_cars(cars_collection: Collection):
   res = list(cars_collection.find())
   assert len(res) == 45
