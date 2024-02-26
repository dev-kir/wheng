from flask import Flask, Blueprint, render_template, redirect, url_for, request

main = Blueprint('main', __name__, template_folder='templates')
# home = Blueprint('home', __name__, template_folder='templates')

# @home.route('/')
# def home_route():
#     return render_template('home.html')

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/test')
def test():
    return render_template('cuba.html')