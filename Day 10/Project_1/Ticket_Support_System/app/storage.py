import json


def load_tickets(file_path):
    with open(file_path, "r") as file:
        return json.load(file)