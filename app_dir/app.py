import os
from datetime import datetime

from flask import Flask
from flask import jsonify
from flask import request
from flask_pymongo import PyMongo

app = Flask(__name__)


MONGO_URI =  os.environ.get('MONGO_URI')
if not MONGO_URI:
    MONGO_URI =  'mongodb://localhost:27017/py_test'

app.config['MONGO_DBNAME'] = 'py_test'
app.config['MONGO_URI'] = MONGO_URI

mongo = PyMongo(app)

@app.route('/report', methods=['GET'])
def get_all_data():
    data = mongo.db.temp_measurements
    output = []
    for s in data.find():
        output.append({
            'id' : s['id'], 
            'timestamp' : s['timestamp'], 
            'temperature' : s['temperature'], 
            'duration' : s['duration']
            })
    if len(output) == 0:
        output.append({
            'error': 'No data present'
        })

    log = mongo.db.log
    new_log = log.insert_one({
        'date_time_requested': datetime.now(),
        'data-size served': data.count()
    })
    
    return jsonify({'result':output})

@app.route('/log', methods=['GET'])
def get_log():
    log = mongo.db.log
    output =[]
    logs = log.find()
    for log in logs:
        output.append({
            'date_time_requested':log['date_time_requested'],
            'data-size served': log['data-size served']
        })
    return jsonify({'result':output})




if __name__ == '__main__':
    app.run(debug=True)