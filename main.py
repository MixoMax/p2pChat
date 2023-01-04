import math
import time
import socket
import requests
import json
from ExitHandler import *
import hashlib

#peer to peer chat
global SERVER_IP, PORT
SERVER_IP = "localhost"
PORT = 54587


def get_IP():
    R = requests.get("http://ip-api.com/json").json()
    IP = R["query"]
    PORT = 54587
    ADDRESS = str(IP) + ":" + str(PORT)
    LOC_COUNTRY = R["country"]
    STATUS = True if R["status"] == "success" else False
    return ADDRESS, LOC_COUNTRY, STATUS

def Register_IP(ADDRESS, LOC_COUNTRY, STATUS):
    if STATUS:
        print("\tSending to", SERVER_IP, "on port", PORT)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #set a timeout so the socket does not block indefinitely when trying to connect
        s.settimeout(2)
        try:
            s.connect((SERVER_IP, 54587))
            s.sendall(bytes(str(str(ADDRESS) + ";" + str(LOC_COUNTRY)), "utf-8"))
            print("\tregistered as " + str(ADDRESS) + " in " + str(LOC_COUNTRY))
            s.close()
        except TimeoutError:
            print(Exit_Code(3))
            print(help(3))
            exit(3)
            
    else:
        print(Exit_Code(2))
        print(help(2))
        exit(2)

def send_message(message, ADDRESS):
    IP = ADDRESS.split(":")[0]
    uuid = hashlib.sha256(str(IP).encode("utf-8")).hexdigest()
    data = [str(IP),str(uuid), str(message)]
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(2)
    try:
        s.connect((SERVER_IP, 54587))
        s.sendall(bytes(str(message), "utf-8"))
        s.close()
    except TimeoutError:
        print(Exit_Code(3))
        print(help(3))
        exit(3)

def main():
    t1 = time.time()
    ADDRESS, LOC_COUNTRY, STATUS = get_IP()
    t2 = time.time()
    print(str(math.floor((t2 - t1) * 1000)) + "ms\tto get IP")
    Register_IP(ADDRESS, LOC_COUNTRY, STATUS)
    t3 = time.time()
    print(str(math.floor((t3 - t2) * 1000)) + "ms\tto register IP")
    message = input("Enter message: ")
    send_message(message, ADDRESS)


if __name__ == "__main__":
    main()