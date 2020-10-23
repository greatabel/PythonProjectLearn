from flask import Blueprint, render_template

from movie.adapters.data_from_memory import load_movies
from movie.domain.model import Director


home_blueprint = Blueprint(
    'home_bp', __name__)


@home_blueprint.route('/', methods=['GET'])
def home():
    movie_list = load_movies()
    # 1, and 2
    director1 = Director("Joss Whedon")
    print(director1)
    # 3, 4
    director2 = Director("Anthony Russo")
    print(director2)
    directors = [director1, director2]
    return render_template(
        'home.html',
        movie_list=movie_list,
        directors=directors,
    )
