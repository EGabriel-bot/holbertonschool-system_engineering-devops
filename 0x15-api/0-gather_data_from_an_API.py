#!/usr/bin/python3
"""Using a REST API return information about TO-DO list progress"""
from curses.ascii import isdigit
import json
import requests
import sys

tasks_done = 0
completed_tasks = []
total_tasks = 0

"""Get request to fetch users"""
if __name__ == "__main__":
    if sys.argv[1].isdigit() is True:
        user = requests.get(
            'https://jsonplaceholder.typicode.com/users/{}'.format(int(sys.argv[1])))

        """Get request to fetch the todo tasks"""
        response = requests.get(
            'https://jsonplaceholder.typicode.com/todos/')

        """Converting data from user and todos to a string dictionary"""
        users = json.loads(user.text)
        tasks_list = json.loads(response.text)

        """Iterating through todo list"""
        for tasks in tasks_list:
            if users['id'] == tasks['userId']:
                if tasks['completed'] is True:
                    completed_tasks.append(tasks['title'])
                    tasks_done += 1
                total_tasks += 1

        print('Employee {} is done with tasks({}/{}:)'
              .format(users['name'], tasks_done, total_tasks))

        for tasks in completed_tasks:
            print('\t {}'.format(tasks))
