import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_PATH = os.path.join(BASE_DIR, "task.json")


def load_tasks():
    try:
        with open(FILE_PATH, "r") as file:
            return json.load(file)
    except:
        return []


def save_tasks(tasks):
    with open(FILE_PATH, "w") as file:
        json.dump(tasks, file, indent=4)

EXPENSE_FILE = os.path.join(BASE_DIR, "expense.json")


def load_expenses():
    try:
        with open(EXPENSE_FILE, "r") as file:
            return json.load(file)
    except:
        return []


def save_expenses(expenses):
    with open(EXPENSE_FILE, "w") as file:
        json.dump(expenses, file, indent=4)