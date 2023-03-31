#!/usr/bin/python3
"""
This script takes in a URL, sends a request to the URL
and displays the value of the X-Request-Id variable
found in the header of the response.
"""
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]
    response = requests.get(url)
    header_value = response.headers['X-Request-Id']
    print(header_value)
