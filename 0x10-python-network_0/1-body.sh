#!/bin/bash
# This script displays the body of the response.
if [[ $(curl -s -o /dev/null -w "%{http_code}" "$1") == 200 ]]; then curl -s "$1"; fi
