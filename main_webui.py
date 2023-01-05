if 0 == 0:
    import math
    import time
    import subprocess
    import json

    try:
        import socket
    except:
        subprocess.run(["pip", "install", "socket"])
    try:
        import requests
    except:
        subprocess.run(["pip", "install", "requests"])
    try:
        from ExitHandler import *
        from main import *
    except:
        exit(1)
    try:
        import zlib
    except:
        subprocess.run(["pip", "install", "zlib"])
    try:
        import os
    except:
        subprocess.run
    try:
        from flask import Flask, request, render_template
    except:
        subprocess.run(["pip", "install", "flask"])
        from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def home():
  return "Hello, World!"

@app.route("/form", methods=["GET", "POST"])
def form():
    if request.method == "POST":
        # Get the form data
        input_field = request.form["input_field"]

        # Process the form data
        t1 = time.time()
        ADDRESS, LOC_COUNTRY, STATUS = get_IP()
        t2 = time.time()
        print(str(math.floor((t2 - t1) * 1000)) + "ms\tto get IP")
        Register_IP(ADDRESS, LOC_COUNTRY, STATUS)
        t3 = time.time()
        print(str(math.floor((t3 - t2) * 1000)) + "ms\tto register IP")
        
        # Render the output template
        return render_template(r"C:\Users\Linus\Desktop\Programming\_Github\p2pChat\_output.html", input_field=input_field)

    return render_template(r"C:\Users\Linus\Desktop\Programming\_Github\p2pChat\_form.html")

if __name__ == "__main__":
    app.run(debug=True)