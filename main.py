import math
import time
import socket
import requests
import json
from ExitHandler import *

#peer to peer chat


def Register_IP():
    IP = requests.get("https://api.ipify.org").text
    PORT = 54587
    ADDRESS = str(IP) + ":" + str(PORT)
    print(ADDRESS)
    
    LOC = requests.get("http://ip-api.com/json/" + str(IP)).json()
    STATUS = True if LOC["status"] == "success" else False
    LOC_COUNTRY = LOC["country"]
    #send to server
    if STATUS:
        print("Sending to server...")
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #set a timeout so the socket does not block indefinitely when trying to connect
        s.settimeout(2)
        try:
            s.connect(("MixoMax.kozow.com", 54587))
            s.sendall(bytes(str(str(ADDRESS) + ";" + str(LOC_COUNTRY)), "utf-8"))
            print("registered as " + str(ADDRESS) + " in " + str(LOC_COUNTRY))
            s.close()
        except TimeoutError:
            print(Exit_Code(3))
            print(help(3))
            raise TimeoutError
    else:
        print(Exit_Code(2))
        print(help(2))

def main():
    Register_IP()


if __name__ == "__main__":
    main()