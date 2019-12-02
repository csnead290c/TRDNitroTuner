from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    title = "Login"
    return render_template('login.html', title=title)

@app.route('/login', methods=["POST"])
def login():
    email = request.form.get("email")
    password = request.form.get("password")
    title = "Welcome!"
    if not email or not password:
        return "failure"
    return render_template('index.html', title=title)

@app.route('/tuningprogram')
def tuningprogram():
    title = "Tuning Program"
    return render_template('index.html', title=title)

@app.route('/runbook')
def runbook():
    title = "Run Book"
    return render_template('index.html', title=title)

@app.route('/weather')
def weather():
    title = "Weather"
    return render_template('index.html', title=title)

@app.route('/fcdownforce')
def fcdownforce():
    title = "FC Downforce"
    return render_template('index.html', title=title)

@app.route('/tfdownforce')
def tfdownforce():
    title = "TF Downforce"
    return render_template('index.html', title=title)

@app.route('/etpredictor')
def etpredictor():
    title = "ET Predictor"
    return render_template('index.html', title=title)

@app.route('/clutch')
def clutch():
    title = "Clutch"
    return render_template('index.html', title=title)

@app.route('/setup')
def setup():
    title = "Setup"
    return render_template('index.html', title=title)

@app.route('/about')
def about():
    title = "About"
    return render_template('about.html', title=title)
