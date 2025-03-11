from flask import Flask, render_template, request, redirect, url_for, jsonify
import requests
from pymongo import MongoClient

app = Flask(__name__)

CONNECTION_STRING = 
client = MongoClient(CONNECTION_STRING)
db = client["SoftwareEngineeringI"]
collection = db["players"]

# Add a player to database
@app.route("/add-player", methods=["POST"])
def add_player():
    new_player = request.json

    collection.insert_one(new_player)

    return {"success": True}

if __name__ == "__main__":
    app.run(port = 4000, debug = True)