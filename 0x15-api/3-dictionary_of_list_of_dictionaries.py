#!/usr/bin/python3
"""
a Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
export data in the JSON format.
"""

import json
import requests

if __name__ == "__main__":
    url_user = "https://jsonplaceholder.typicode.com/users"
    url_todos = "https://jsonplaceholder.typicode.com/todos"
    response_details = requests.get(url=url_user)
    response_todos = requests.get(url=url_todos)
    data_details = response_details.json()
    data_todos = response_todos.json()
    # print(data_todos)
    todos_obj = {
        data1.get('id'): [
            {'username': data1.get('username'),
             'task': data2.get('title'),
             'completed': data2.get('completed')}
            for data2 in data_todos if data2.get('userId') is data1.get('id')
        ] for data1 in data_details
    }
    with open(f"todo_all_employees.json", "w") as file:
        json.dump(todos_obj, file, indent=4)
