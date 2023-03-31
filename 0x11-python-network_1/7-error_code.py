#!/usr/bin/python3
"""
This script takes in a URL, sends a request to the
URL and displays the body of the response (decoded in utf-8).
"""
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]
    response = requests.get(url)
    try:
        response.raise_for_status()
        content = response.text
        print(content)
    except requests.exceptions.HTTPError:
        print('Error code: {}'.format(response.status_code))
