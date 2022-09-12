#!/usr/bin/python3
"""Using a REST API return information about TO-DO list progress"""
import json
import requests
import sys

if __name__ == "__main__":
    if sys.argv[1].isdigit() is True:
        idd = int(sys.argv[1])

        """Get request to fetch users"""
        user = requests.get(
            'https://jsonplaceholder.typicode.com/users/{}'.format(idd))

        """Get request to fetch the todo tasks"""
        response = requests.get(
            'https://jsonplaceholder.typicode.com/todos/')

        """Converting data from user and todos to a string dictionary"""
        users = json.loads(user.text)
        tasks_list = json.loads(response.text)

        tasks_done = 0
        completed_tasks = []
        total_tasks = 0
        """Iterating through todo list"""
        for tasks in tasks_list:
            if users['id'] == tasks['userId']:
                total_tasks += 1
                if tasks['completed'] is True:
                    completed_tasks.append(tasks['title'])
                    tasks_done += 1

        print('Employee {} is done with tasks({}/{}:)'
              .format(users['name'], tasks_done, total_tasks))

        for tasks in completed_tasks:
            print('\t {}'.format(tasks))
