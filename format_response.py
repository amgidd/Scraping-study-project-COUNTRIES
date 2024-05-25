# from collections import namedtuple
from parse_response import get_countries
# import sys


def get_sorted_countries() -> list:
    rr = get_countries()
    return sorted(rr, key=lambda rr: rr.population, reverse=True)

if __name__ == "__main__":
    rs = get_sorted_countries()

    for item in rs:
        print(item)
