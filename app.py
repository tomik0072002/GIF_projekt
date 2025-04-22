from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/action', methods=['POST'])
def action():
    button = request.form['button']
    return f"Stiskl jsi: {button}"

if __name__ == '__main__':
    app.run(debug=True)
