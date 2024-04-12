from server import app
#from flask import render_template
from controllers.control import home, register_user, register_page, consult_page, consult_user

@app.route('/')
def func_home():
    return home()

@app.route("/register_user", methods=["POST"])
def func_register_user():
    return register_user()

@app.route("/register_page")
def func_register_page():
    return register_page()

@app.route("/consult_page")
def func_consult_page():
    return consult_page()

@app.route("/consult_user", methods=["POST"])
def func_consult_user():
    return consult_user()