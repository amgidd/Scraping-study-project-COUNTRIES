from bs4 import BeautifulSoup
# import sys
from collections import namedtuple
from get_response import get_response

def get_countries() -> list:
    soup = BeautifulSoup(get_response().text, "html.parser")

    countries1 = soup.find_all("h3", class_ = "country-name")
    capitals1 = soup.find_all("span", class_ = "country-capital")
    populations1 = soup.find_all("span", class_ = "country-population")
    areas1 = soup.find_all("span", class_ = "country-area")

    Country = namedtuple("Country", "name, capital, population, area")
    countries = []
    for item in zip(countries1, capitals1, populations1, areas1):
        country = Country(*map(lambda i: i.text.strip(), item))
        countries.append(country)
    return countries

if __name__== "__main__":

    rr = get_countries()

    print(rr[0], end="\n\n")
