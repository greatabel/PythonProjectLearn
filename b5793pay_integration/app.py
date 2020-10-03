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


products = get_products()


@app.route('/')
def cart_list():
    return render_template('index.html', products=products)


@app.route('/shopping_cart/<productid>')
def shopping_list(productid):
    product = products[int(productid)]
    print('productid=', productid)
    return render_template('shopping_cart.html', product=product)


@app.route('/payment/<total>')
def payment(total):
    print('total=', total)
    return render_template('payment.html', total=total)


@app.route('/paypal/<total>')
def paypal(total=1):
    print('total=', total)
    return render_template('paypal.html', total=total)