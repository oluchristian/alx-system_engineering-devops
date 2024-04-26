#!/usr/bin/python3
import json
import requests
import sys

if __name__ == "__main__":
    employeeId = sys.argv[1]
    if (type(int) == employeeId):
        r = requests.get('https://jsonplaceholder.typicode.com/todos/employeeId');
		payload = r.json();
		python_dict = json.loads(payload);
		employee_name = python_dict["EMPLOYEE_NAME"];
		tasksDone = python_dict["NUMBER_OF_DONE_TASKS"]
		print("Employee payload() is done with tasks(NUMBER_OF_DONE_TASKS/TOTAL_NUMBER_OF_TASKS):")
