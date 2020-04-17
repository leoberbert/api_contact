#!/usr/bin/python3
# -*- coding: utf-8 -*-

from flask import Flask
from flask import request
from flask import jsonify
from pymongo import MongoClient
from bson.json_util import dumps
import json
import socket

#client = MongoClient('localhost:27017')
client = MongoClient('mongo_db:27017')
db = client.ContactDB

app = Flask(__name__)

@app.route("/add_contact", methods = ['POST'])

def add_contact():
    try:
        data = json.loads(request.data)
        user_name = data['name']
        user_contact = data['contact']
        
        if user_name and user_contact:
            check_exist = check_contract(user_contact)
            if check_exist == 1:
                return jsonify({'message' : 'ERROR - The contact '  + str(user_contact) +  ' already exists.'}) 
            else:
                status = db.Contacts.insert_one({
                "name" : user_name,
                "contact" : user_contact
                })
                return jsonify({'message' : 'SUCCESS'})

    except Exception as e:
        return jsonify({'error' : str(e)})

def check_contract(user_contact):
    try:
        if db.Contacts.find({"contact" : user_contact}).count() > 0 :
            return(1)
        else:
            return(0)
        
    except Exception as e:
        return jsonify({'error' : str(e)})

@app.route("/get_contact", methods = ['GET'])

def get_contact():
    try:
        data = json.loads(request.data)
        user_contact = data['contact']
        check_exist = check_contract(user_contact)
        if check_exist == 1:
            contacts = db.Contacts.find({"contact": user_contact})
            return dumps(contacts)
        else:
            return jsonify({'message' : 'ERROR - The contact '  + str(user_contact) +  ' do not exist.'}) 
    except Exception as e:
        return dumps({'error' : str(e)})

if __name__ == '__main__':
    hostname=socket.gethostname()
    localIP=socket.gethostbyname(hostname)
    app.run(host=localIP, port=5000)
