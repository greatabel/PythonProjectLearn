from flask import Flask, jsonify, request


app = Flask(__name__)

recipes = [
    {
        'id': 1,
        'name': 'Egg Salad',
        'description': 'This is a lovely egg salad recipe.'
    },
    {
        'id': 2, 'name': 'Tomato Pasta',
        'description': 'This is a lovely tomato pasta recipe.'
    }
]


@app.route("/recipes", methods=['GET'])
def get_recipes():
    return jsonify({'data': recipes})


if __name__ == "__main__":
    app.run()