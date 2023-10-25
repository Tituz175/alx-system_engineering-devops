#!/usr/bin/python3
"""
a Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
export data in the JSON format.
"""

import csv
import json
import requests
import sys

if __name__ == "__main__":
    id = sys.argv[1]
    url_user = "https://jsonplaceholder.typicode.com/users"
    url_todos = "https://jsonplaceholder.typicode.com/todos"
    params_detail = {"id": id}
    params_todo = {"userId": id}
    response_details = requests.get(url=url_user, params=params_detail)
    response_todos = requests.get(url=url_todos, params=params_todo)
    data_details = response_details.json()[0]
    data_todos = response_todos.json()
    user_obj = {id: [{'task': data.get('title'),
                      'completed': data.get('completed'),
                      'username': data_details.get('username')
                      } for data in data_todos]}
    with open(f"{id}.json", "w") as file:
        json.dump(user_obj, file, indent=4)
