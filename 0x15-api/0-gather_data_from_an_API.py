#!/usr/bin/python3
"""python script for a given employee ID, that returns information"""
import requests
import sys


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com"
    user_id = int(sys.argv[1])
    user_endP = "{}/users/{}".format(url, user_id)
    name = requests.get(user_endP).json().get("name")
    tasks_endP = "{}/todos".format(url)
    tasks = requests.get(tasks_endP).json()
    user_tasks = [task for task in tasks if task.get("userId") == user_id]
    completed_tasks = [task for task in user_tasks if task.get("completed")]
    print("Employee {} is done with tasks({}/{}):"
          .format(name, len(completed_tasks), len(user_tasks)))

    for task in completed_tasks:
        print("\t {}".format(task.get("title")))
