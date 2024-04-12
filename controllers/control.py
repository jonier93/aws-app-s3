from flask import Flask, render_template, request, jsonify
from database.db_customers import insert_record, consult_record

def home():
    return render_template('home.html')

def register_page():
    return render_template("register.html")

def register_user():
    obj = request.get_json()    
    validation = insert_record(obj["name"], obj["id"], obj["age"])
    if validation:
        data = {'message':"ok"}
        return jsonify(data) 
    else:
        data = {'message':"error"}
        return jsonify(data) 

def consult_page():
    return render_template("consult.html")

def consult_user():
    obj = request.get_json()
    results = consult_record(obj["id"])
    if len(results) == 0:    
        print("no existe el registro")
        data = {'message':"error"}
        return jsonify(data) 
    else:
       return jsonify(results) 