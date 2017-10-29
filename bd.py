from flask import Flask, render_template, request
from datetime import datetime
from pymongo import MongoClient
from flask import jsonify
import json

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/d")
def d():
    return request.body.args("name")

@app.route('/data')
def data():
    st1=[]
    dat= client["pene2"].test.find()
    for i in dat:
        return str(dat)


if __name__ == "__main__":
    client = MongoClient('localhost', 27017)
    print("\n\nConnected to localhost:27017\n")
    app.run()


