from dotenv import load_dotenv
import os
import requests
import json

load_dotenv()

session_id = os.getenv("SESSION_ID", "")


def clean_data(data: str, splitVal: str) -> list[str]:
    try:
        return [x.strip() for x in data.split(splitVal) if len(x.strip()) > 0]
    except Exception as e:
        print(f"Error cleaning data: {e}")
        raise


def get_data(day: int, splitVal: str) -> list[str]:
    url = f"https://adventofcode.com/2025/day/{day}/input"
    cookie = {"session": session_id}

    try:
        response = requests.get(url, cookies=cookie)
        return clean_data(response.text, splitVal)
    except Exception as e:
        print(f"Error fetching test data: {e}")
        raise


def get_test_data(day: int, splitVal: str) -> list[str]:
    try:
        with open("test_data/db.json", "r") as file:
            data = json.load(file)
            key = f"day{str(day).zfill(2)}"
            return clean_data(data[key], splitVal)
    except Exception as e:
        print(f"Error fetching test data: {e}")
        raise


def printf(o) -> None:
    print(json.dumps(o, indent=2))
