import pytest
from pymongo.collection import Collection




@pytest.fixture(scope="function")
def driver_collection(init_test_data):
   return init_test_data['drivers']


def test_find_all_drivers(driver_collection: Collection):
   res = list(driver_collection.find())
   print(res)
   assert len(res) == 30
