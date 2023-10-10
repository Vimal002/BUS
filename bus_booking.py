from flask import Flask, render_template, request
from login import *

app = Flask(__name__)

buses = [
    {
        "bus_id": 1,
        "bus_name": "ABC Bus",
        "price": 10,
        "seats": 50
    },
    {
        "bus_id": 2,
        "bus_name": "XYZ Bus",
        "price": 15,
        "seats": 60
    }
]

@app.route("/")
def index():
    
    return render_template("index.html", buses=buses)

@app.route("/book", methods=["POST"])
def book():
    bus_id = int(request.form["bus_id"])
    bus = next((b for b in buses if b["bus_id"] == bus_id), None)
    if bus and bus["seats"] > 0:
        bus["seats"] -= 1
        return render_template("success.html", bus=bus)
    else:
        return render_template("error.html")

if __name__ == "__main__":
    app.run()
