from flask import render_template
from random import choice
from datetime import datetime
from datetime import timedelta

from FlaskWebProject import app
from FlaskWebProject.globals import cars_list
from FlaskWebProject.globals import cats_list
from FlaskWebProject.globals import counter_visits
from FlaskWebProject.globals import words


@app.route('/hello_world')
def hello_world():
    return render_template('HelloWorld.html')


@app.route('/cars')
def cars():
    return render_template('Cars.html', cars = cars_list)

@app.route('/cats')
def cats():
    cat = choice(cats_list)
    return render_template('Cats.html', cat = cat)


@app.route('/get_time/now')
def get_time_now():
    now = datetime.now()
    time_now = get_time(now.hour, now.minute, now.second)
    return render_template('DateTimeNow.html', current_time = time_now)


@app.route('/get_time/future')
def get_time_future():
    now = datetime.now()
    delta = now + timedelta(hours=1)
    time_future = get_time(delta.hour, delta.minute, delta.second)
    return render_template('DateTimeFuture.html', current_time_after_hour = time_future)


@app.route('/get_random_word')
def get_random_word():
    word = choice(words)
    return render_template('RandomWord.html', random_word = word)


@app.route('/counter')
def counter():
    counter_visits.visits += 1
    return render_template('Counter.html', counter = counter_visits.visits)


def get_time(hours, minutes, seconds):
    return str(hours) + ':' + str(minutes) + ':' + str(seconds)