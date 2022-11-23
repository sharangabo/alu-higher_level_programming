#!/usr/bin/python3
"""A python script that takes in a url,
sends a request to url and displays the body of the
response decoded in utf-8"""
import urllib.request
import sys


if __name__ == "__main__":
    try:
        with urllib.request.urlopen(sys.argv[1]) as response:
            body = response.read()
            print(body.decode("utf-8"))
    except urllib.error.HTTPError as error:
        print("Error code: {}".format(error.code))
