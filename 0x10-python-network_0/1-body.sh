#!/bin/bash
# This script displays the body of the response.
if [[ $(curl -sL -o /dev/null -w "%{http_code}" "$1") == 200 ]]; then curl -sL "$1"; fi
