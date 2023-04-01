#!/usr/bin/python3
"""
This script takes your GitHub credentials and uses
the GitHub API to display latest commits.
"""
import sys
import requests


if __name__ == "__main__":
    repo = sys.argv[1]
    owner = sys.argv[2]
    url = f'https://api.github.com/repos/{owner}/{repo}/commits?per_page=10'

    response = requests.get(url)
    commits = response.json()
    for commit in (commits):
        sha = commit['sha']
        author_name = commit['commit']['author']['name']
        print(f'{sha}: {author_name}')
