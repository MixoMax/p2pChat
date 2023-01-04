import requests
import json
import timeit
import math

def get_IP():
    t_dyndns = timeit.timeit(_dydnds, number=1)
    t_ipify = timeit.timeit(_ipify, number=1)
    t_ipinfo = timeit.timeit(_ipinfo, number=1)
    t_ipecho = timeit.timeit(_ipecho, number=1)
    t_ipapi = timeit.timeit(_ipapi, number=1)
    t_myexternalip = timeit.timeit(_myexternalip, number=1)
    t = [t_dyndns, t_ipify, t_ipinfo, t_ipecho, t_ipapi, t_myexternalip]
    minidx = t.index(min(t))
    p = ["dyndns", "ipify", "ipinfo", "ipecho", "ipapi", "myexternalip"]
    for i in range(len(t)):
        print(str(math.floor(t[i] * 1000)) + "ms\t" + p[i])
    return p[minidx]
    
    

def _dydnds():
    r = requests.get("http://checkip.dyndns.org")
    return r.text.strip()

def _ipify():
    r = requests.get("https://api.ipify.org")
    return r.text.strip()

def _ipinfo():
    r = requests.get("https://ipinfo.io")
    return r.json()

def _ipecho():
    r = requests.get("https://ipecho.net/plain")
    return r.text.strip()

def _ipapi():
    r = requests.get("http://ip-api.com/json")
    return r.json()

def _myexternalip():
    r = requests.get("https://myexternalip.com/json")
    return r.json()

if __name__ == "__main__":
    print(get_IP())