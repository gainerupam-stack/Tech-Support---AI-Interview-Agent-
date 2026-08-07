import json
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

DATA_DIR = os.path.join(BASE_DIR, "data")


def load_curriculum():

    path = os.path.join(DATA_DIR, "curriculum.json")

    with open(path, "r", encoding="utf-8") as file:
        return json.load(file)


def load_candidates():

    path = os.path.join(DATA_DIR, "candidates.json")

    with open(path, "r", encoding="utf-8") as file:
        return json.load(file)