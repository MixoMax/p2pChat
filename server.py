import socket
import requests
import csv

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
    with open("./cache/IPs.csv", "a") as file:
        writer = csv.writer(file)
        if not check_if_IP_in_file(IP):
            writer.writerow([IP, PORT, COUNTRY])
            print(IP, "added to file")

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

def main():
    while True:
        IP, REST = Listen_for_IP().split(":")
        PORT, COUNTRY = REST.split(";")
        write_to_file(IP, PORT, COUNTRY)

if __name__ == "__main__":
    main()