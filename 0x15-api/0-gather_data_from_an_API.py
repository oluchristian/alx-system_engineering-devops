#!/usr/bin/python3
"""Retrieve and display todo list progress for a given employee ID.
"""
import json
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(1)
    try:
        employeeId = int(sys.argv[1])
    except ValueError:
        sys.exit(1)
    user_url = f"https://jsonplaceholder.typicode.com/users/{employeeId}"
    todo_url = user_url + "/todos"
    r_user = requests.get(user_url)
    user = r_user.json()
    user_name = user.get('name')
    r_todos = requests.get(todo_url)
    todos = r_todos.json()
    todo_num = len(todos)
    completed = sum(1 for todo in todos if todo.get("completed"))
    print(f"Employee {user_name} is done with tasks({completed}/{todo_num}):")
    for todo in todos:
        if todo['completed']:
            print(f"\t{todo['title']}")
