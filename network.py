#!/usr/bin/env python3

import requests
import socket

def check_localhost():
    """Checks whether the local host is correctly configured"""
    localhost = socket.gethostbyname('localhost')
    #return localhost == "127.0.0.1"
    return localhost

def check_connectivity():
    """Checks whether the computer can make successful calls to the internet"""
    url = "http://www.google.com"
    request = requests.get(url)
    return request.status_code
    #print(request.text)

if not check_localhost() == "127.0.0.1" and not check_connectivity() == "200":
    print("False")
else:
    #print(check_localhost(), end = "\n")
    print("True")

#print("check_connectivity(url) == 'http://www.google.com'")
