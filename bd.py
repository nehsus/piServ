from flask import Flask, render_template, request
from datetime import datetime
from pymongo import MongoClient
import jsonify
import json

mseal = MongoClient("localhost, 27017")
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")
@app.route("/d")
def d():
    return request.body.args("name")

@app.route("/data")
def data():
    str1=[]
    tim = mseal["pene2"].tables.find()
    for i in tim:
        str1.append(i)
    return str(str1).replace("'", "\"")

if __name__ == "__main__":
    app.run()
