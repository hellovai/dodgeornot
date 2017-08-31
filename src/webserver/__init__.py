"""
Basic module which creates the app
"""
from flask import Flask
myApp = Flask(__name__)

@myApp.route('/')
def hello_world():
    return 'Hello, World!'
