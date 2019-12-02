from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
def hello_world():
    title = "TRD Tuning Program"
    return render_template('index.html', title=title)

@app.route('/data')
def data():
    return 'test'
