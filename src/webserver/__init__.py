"""
Basic module which creates the app
"""
from flask import Flask, render_template, url_for, request

myApp = Flask(__name__)

@myApp.route('/')
def hello_world():
    return render_template("entry.html")

@myApp.route('/process_summoner_names', methods=["GET"])
def process_summoner_names():
    summoner_names = [
        request.args.get('summoner1'),
        request.args.get('summoner2'),
        request.args.get('summoner3'),
        request.args.get('summoner4'),
        request.args.get('summoner5')
    ]
    return str(summoner_names)