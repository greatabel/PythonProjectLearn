from flask import Flask
from flask import Blueprint, render_template


# from movie.adapters.memory_repository import load_movies
import movie.adapters.repository as repo
from movie.domain.model import Director, User


home_blueprint = Blueprint(
    'home_bp', __name__)


class PageResult:
    
    def __init__(self, data, page=1, number=2):
        self.__dict__ = dict(zip(['data', 'page', 'number'], [data, page, number]))
        self.full_listing = [self.data[i:i+number] for i in range(0, len(self.data), number)]

    def __iter__(self):
        if self.page - 1 < len(self.full_listing):
            for i in self.full_listing[self.page-1]:
                yield i
        else:
            return None

    def __repr__(self): #used for page linking
        return "/home/{}".format(self.page+1) #view the next page



@home_blueprint.route('/home/<int:pagenum>', methods=['GET'])
def home(pagenum):
    movie_list = []
    movie_list = repo.repo_instance.load_movies()
    # movie_list = load_movies()
    # 1, and 2
    director1 = Director("Joss Whedon")

    # 3, 4
    director2 = Director("Anthony Russo")

    directors = [director1, director2]

    return render_template(
        'home.html',
        listing=PageResult(movie_list, pagenum),
        directors=directors,
    )


