from flask import Flask, request, jsonify
import json

app = Flask(__name__)

@app.route('/register', methods=['GET','POST'])
def main():
    if request.method == 'POST':
        json_data = request.get_json()
        return jsonify(json_data)
        
     
    if request.method == 'GET':
        return "GET обработан"