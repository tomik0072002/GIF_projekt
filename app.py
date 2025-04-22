from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/action', methods=['POST'])
def action():
    button = request.form['button']
    return f"Stiskl jsi: {button}"
