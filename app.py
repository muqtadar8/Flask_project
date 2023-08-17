from flask import Flask

app = Flask(__name__)


@app.route("/")

def home():
    return "This is Home Page"

if __name__ == '__main__':
    app.run(debug = True,host = '172.18.181.148')


