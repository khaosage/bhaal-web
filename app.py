#!/usr/env/python

from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/test')
def test():
    return render_template('test.html')



@app.route('/about_us')
def about_us():
    return render_template('about_us.html')


@app.route('/raid_info')
def raid_info():
    return render_template('raid_info.html')


@app.route('/raid_progress')
def raid_progress():
    return render_template('raid_progress.html')


@app.route('/raid_format')
def raid_format():
    return render_template('raid_format.html')


@app.route('/epgp')
def epgp():
    return render_template('epgp.html')


@app.route('/recruitment')
def recruitment():
    return render_template('recruitment.html')


@app.route('/naxxramas')
def naxxramas():
    return render_template('naxxramas.html')


@app.route('/sartharion')
def sartharion():
    return render_template('sartharion.html')


@app.route('/ulduar')
def ulduar():
    return render_template('ulduar.html')


if __name__ == '__main__':
    app.run(debug=True)
