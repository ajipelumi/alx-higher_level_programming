#!/usr/bin/python3
"""
This script takes your GitHub credentials (username
and password) and uses the GitHub API to display your repos.
"""
import sys
import requests


if __name__ == "__main__":
    repo = sys.argv[1]
    owner = sys.argv[2]
    url = f'https://api.github.com/repos/{owner}/{repo}/commits'

    response = requests.get(url)
    content = response.json()
    for idx in range(10):
        data = content[idx]
        print(f'{data["sha"]}: {data["commit"]["author"]["name"]}')
