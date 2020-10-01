from flask import Flask
from flask import render_template


app = Flask(__name__)


@app.route('/')
def cart_list():
    return render_template('index.html')
