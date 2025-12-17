from dotenv import load_dotenv
import os
import requests
import json

load_dotenv()

session_id = os.getenv("SESSION_ID", "")


def clean_data(data: str, split_val: str) -> list[str]:
    """Cleans the input data by splitting it using the specified delimiter
    and stripping whitespace from each element."""
    try:
        return [x.strip() for x in data.split(split_val) if len(x.strip()) > 0]
    except Exception as e:
        print(f"Error cleaning data: {e}")
        raise


def clean_data_multipart(data: str, split_val: str) -> list[list[str]]:
    """Cleans the input data by splitting it using the specified delimiter
    and stripping whitespace from each element where directions are divided."""
    try:
        top, bottom = data.split("\n\n")
        return [
            [x.strip() for x in top.split(split_val) if len(x.strip()) > 0],
            [x.strip() for x in bottom.split(split_val) if len(x.strip()) > 0],
        ]
    except Exception as e:
        print(f"Error cleaning data: {e}")
        raise


def get_data(day: int, split_val: str, type: str = "full") -> list[str]:
    """Fetches the input data for the specified day"""
    url = f"https://adventofcode.com/2025/day/{day}/input"
    cookie = {"session": session_id}

    try:
        if type == "test":
            with open("test_data/db.json", "r") as file:
                data = json.load(file)
                key = f"day{str(day).zfill(2)}"
                return clean_data(data[key], split_val)
        else:
            response = requests.get(url, cookies=cookie)
            return clean_data(response.text, split_val)
    except Exception as e:
        print(f"Error fetching data: {e}")
        raise


def get_data_multipart(day: int, split_val: str, type: str = "full") -> list[list[str]]:
    """Fetches the data for the specified day where directions are divided."""
    url = f"https://adventofcode.com/2025/day/{day}/input"
    cookie = {"session": session_id}

    try:
        if type == "test":
            with open("test_data/db.json", "r") as file:
                data = json.load(file)
                key = f"day{str(day).zfill(2)}"
                return clean_data_multipart(data[key], split_val)
        else:
            response = requests.get(url, cookies=cookie)
            return clean_data_multipart(response.text, split_val)
    except Exception as e:
        print(f"Error fetching data: {e}")
        raise


def printf(o: object) -> None:
    """Prints the given object in a formatted JSON style for better readability."""
    print(json.dumps(o, indent=2))
