#!/usr/bin/python3
"""
This script takes in a letter and sends a POST request
to http://0.0.0.0:5000/search_user with the letter
as a parameter.
"""
import sys
import requests


if __name__ == "__main__":
    # Store url
    url = 'http://0.0.0.0:5000/search_user'

    # Check for argument length
    if len(sys.argv) == 1:
        q = ""
    else:
        q = sys.argv[1]

    # Store element to search in dictionary
    values = {'q': q}

    # Make post request
    response = requests.post(url, data=values)

    # If response json is empty
    if not response.json():
        print('No result')

    # If response json type is not a valid json
    elif response.headers.get('content-type') != 'application/json':
        print('Not a valid JSON')

    # If response json is valid
    else:
        content = response.json()
        print('[{}] {}'.format(content.get('id'), content.get('name')))
