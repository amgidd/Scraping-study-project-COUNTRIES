from typing import Protocol
from pathlib import Path
import json
from format_response import get_sorted_countries

def save_txt(countries: list) -> None:
    with open("results/info.txt", 'w') as f:
        for country in countries:
            f.write("; ".join(country) + "\n")

def save_json(countries: list) -> None:
    with open("results/info.json", 'w') as fstream:
        fstream.write('[')
        for country in countries:
            json.dump(country._asdict(), fstream)
            fstream.write(', ')
    with open("results/info.json", 'rb+') as f:
        f.seek(-2, 2)
        f.truncate()
        f.write(bytes(']', 'utf8'))

def save(storage: str):
    Path.cwd().joinpath("results").mkdir(exist_ok=True)
    if storage == 'txt':
        save_type = save_txt
    elif storage == 'json':
        save_type = save_json
    save_type(get_sorted_countries())

if __name__ == "__main__":
    save('txt')
