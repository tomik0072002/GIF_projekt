from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Ahoj světe z Azure a GitHubu!'

if __name__ == '__main__':
    app.run()
