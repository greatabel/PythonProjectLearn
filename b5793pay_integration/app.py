from flask import Flask
from flask import render_template
import json


app = Flask(__name__)
app.debug = True

def get_products():
    print('get_products', '#'*10)
    # Reading data 
    with open('products.json', 'r') as f:
        products = json.load(f)
        return products
    return None


@app.route('/')
def cart_list():
    products = get_products()
    return render_template('index.html', products=products)
