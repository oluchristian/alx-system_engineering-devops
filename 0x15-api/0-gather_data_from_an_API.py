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
    url = f"https://jsonplaceholder.typicode.com/todos?userId={employeeId}"
    response = requests.get(url)
    todos = response.json()
    todo_number = len(todos)
    task_completed = sum(1 for todo in todos if todo.get("completed"))
    print(f"Employee {employeeId} is done with tasks({task_completed}/{todo_number}):")
    for todo in todos:
        if todo['completed']:
            print(f"\t{todo['title']}")