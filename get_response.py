import requests
from config import URL

def get_response():
    return requests.get(URL)

if __name__ == "__main__":
    print(r.status_code)
    print(type(r))
