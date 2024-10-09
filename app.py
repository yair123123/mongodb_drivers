from functools import partial
from operator import add
from toolz import pipe

from repository.csv_repository import init_taxi_drivers

if __name__ == '__main__':
    init_taxi_drivers()