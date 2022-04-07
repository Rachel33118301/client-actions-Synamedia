#!/usr/bin/python

import json
import os.path
from socket import *
import time
import hashlib
import json
from pathlib import Path

# Assigning server IP and server port
serverName = "0.0.0.0"
serverPort = 5000

# Setting buffer length
buffer_length = 500
# Assigning the audio file a name
file_path = defoult_file = r'./file.txt'
clientSocket = socket(AF_INET, SOCK_DGRAM)

while file_path != "0":
    try:
        file_path = input("enter file location")
    except EOFError as e:
        print(e)
    if file_path == "0":
        break
    try:
        if file_path == "":
            file_path = defoult_file
        file_path = Path(file_path)
    except Exception as e:
        raise Exception('illegal location')
    if not os.path.exists(file_path):
        raise Exception("file doesn't exists")
    f = open(file_path, "rb")
    # Reading the buffer length in data
    file_data = f.read(buffer_length)
    hash = hashlib.md5(file_data).hexdigest()
    data = {'name': file_path.name[:-4], 'file': file_data.decode(), "hash": hash}

    if clientSocket.sendto(json.dumps(data).encode(), (serverName, serverPort)):
        data = f.read(buffer_length)
        time.sleep(0.02)  # waiting for 0.02 seconds
    f.close()
    print("the file sent to server")
clientSocket.close()
