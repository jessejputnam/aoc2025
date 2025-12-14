from dotenv import load_dotenv
import os
import requests
import json

load_dotenv()

session_id = os.getenv("SESSION_ID", "")


def clean_data(data: str, splitVal: str) -> list[str]:
    return [x.strip() for x in data.split(splitVal) if len(x.strip()) > 0]


def get_data(day: int, splitVal: str) -> list[str]:
    url = f"https://adventofcode.com/2025/day/{day}/input"
    cookie = {"session": session_id}

    response = requests.get(url, cookies=cookie)

    return clean_data(response.text, splitVal)


def get_test_data(day: int, splitVal: str):
    with open("test_data/db.json", "r") as file:
        data = json.load(file)
        key = f"day{str(day).zfill(2)}"
        return clean_data(data[key], splitVal)


def printf(o):
    print(json.dumps(o, indent=2))
