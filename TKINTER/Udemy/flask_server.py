from flask import Flask, request, render_template
import requests
r = requests.get('https://raw.githubusercontent.com/Advik-B/Web-Browser/Master/favicon.ico')

app = Flask('app')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/favicon.ico')
def favicon():
    return r.content



app.run('localhost', port='2380')