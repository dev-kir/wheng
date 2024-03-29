from flask import Flask, Blueprint, render_template, redirect, url_for, request, jsonify
import datetime

main = Blueprint('main', __name__, template_folder='templates')
# home = Blueprint('home', __name__, template_folder='templates')

# @home.route('/')
# def home_route():
#     return render_template('home.html')

# target_time = datetime.datetime(2024, 2, 29, 15, 0, 0)
target_time = datetime.datetime(2024, 2, 27, 11, 8, 30)


@main.context_processor
def var():
    event_description = "you're noob"
    event_congratulations = "thank you, noob"
    return dict(
        event_description = event_description,
        event_congratulations = event_congratulations
    )

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/get_remaining_time')
def get_remaining_time():
    current_time = datetime.datetime.now()
    remaining_time = target_time - current_time

    remaining_seconds = max(remaining_time.total_seconds(), 0)
    
    days, seconds = divmod(remaining_seconds, 86400)
    hours, remainder = divmod(seconds, 3600)
    minutes, seconds = divmod(remainder, 60)

    return jsonify({
        'days': f'{int(days):02d}',
        'hours': f'{int(hours):02d}',
        'minutes': f'{int(minutes):02d}',
        'seconds': f'{int(seconds):02d}',
    })

@main.route('/done')
def done():
    current_time = datetime.datetime.now()
    remaining_time = target_time - current_time
    remaining_seconds = max(remaining_time.total_seconds(), 0)

    if remaining_seconds <= 0:
        return render_template('done.html')
    else:
        return redirect(url_for('main.index'))

@main.route('/test')
def test():
    return render_template('cuba.html')