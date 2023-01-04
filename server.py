import socket
import requests
import csv
import sys
import os
import argparse
import time

def Listen_for_IP():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(("localhost", 54587))
        s.listen()
        conn, addr = s.accept()
        with conn:
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                return data.decode("utf-8")

def write_to_file(IP, PORT, COUNTRY):
    #check if file exists
    try:
        open("./cache/IPs.csv", "r")
    except FileNotFoundError:
        os.mknod("./cache/IPs.csv")
    with open("./cache/IPs.csv", "a") as file:
        writer = csv.writer(file)
        if not check_if_IP_in_file(IP):
            writer.writerow([IP, PORT, COUNTRY])
            print(IP, "added to file")
        else:
            print(IP, "already in file")

def check_if_IP_in_file(IP):
    with open("./cache/IPs.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            try:
                if row[0] == IP:
                    return True
            except IndexError:
                return False
        return False

def delete_IP_from_file(IP):
    with open("./cache/IPs.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            try:
                if row[0] == IP:
                    pass
            except IndexError:
                pass
        return False

def clear_file():
    with open("./cache/IPs.csv", "w") as file:
        file.truncate()
    os.mknod("./cache/IPs.csv")
    print("file cleared")

def main(args):
    if(args.clear == 1):
        clear_file()
    while True:
        data = Listen_for_IP()
        if(data.count(":") ==1 and data.count(";") == 1):
            IP, REST = data.split(":")
            PORT, COUNTRY = REST.split(";")
            write_to_file(IP, PORT, COUNTRY)
        else:
            print(data)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Server for p2pChat")
    parser.add_argument("-c", "--clear",type=int, help="clear the IPs file", default=0)
    args = parser.parse_args()
    main(args)