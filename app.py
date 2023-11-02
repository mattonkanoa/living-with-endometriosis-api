import json
from flask import Flask, jsonify, request

app = Flask(__name__)

employees = [ { 'id': 1, 'name': 'Kanoa Matton' }, { 'id': 2, 'name': 'Kai' }, { 'id': 3, 'name': 'Moana' }]

@app.route('/employees', methods=['GET'])
def get_employees():
    return jsonify(employees)