from flask import Flask
from flask import render_template
import json
from flask import request


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

common_n = 23707
public_e = 20981
clients = {'alice': 0, 'bob': 0, 'karen': 0, 'bank': 0}

@app.route('/q2_c_home/<name>')
def bank_check(name):
    flag = False
    if request.args.get('private_d') is not None \
        and request.args.get('message') is not None:
        private_d = int(request.args.get('private_d'))
        message = int(request.args.get('message'))
        if name == 'bank':
            bmessage = clients['alice']
            s = pow(bmessage, private_d) % common_n
            if s == message:
                print('#'*20, 'sign verified success!')
                flag = True
        s = None
        s = pow(message, private_d) % common_n
        clients[name] = s
        print(clients)
    others = ['alice', 'bob', 'karen']
    if name != 'bank':
        others.remove(name)

    return render_template('Q2_c_bank_check.html', name=name, 
                others=others, clients=clients, flag=flag)
