#!/usr/bin/python3
"""
This script takes your GitHub credentials (username
and password) and uses the GitHub API to display your id.
"""
import sys
import requests


if __name__ == "__main__":
    url = 'https://api.github.com/user'
    username = sys.argv[1]
    password = sys.argv[2]

    response = requests.get(url, auth=(username, password))
    content = response.json()
    get_id = content.get('id')
    print(get_id)
