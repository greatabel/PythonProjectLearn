import csv
import os
from datetime import date, datetime
from typing import List

from movie.adapters.repository import AbstractRepository, RepositoryException
from movie.domain.model import Movie



def read_csv_file(filename: str):
    with open(filename, encoding='utf-8-sig') as infile:
        reader = csv.reader(infile)

        # Read first line of the the CSV file.
        headers = next(reader)

        # Read remaining rows from the CSV file.
        for row in reader:
            # Strip any leading/trailing white space from data read.
            row = [item.strip() for item in row]
            yield row


def load_movies():
    data_path = os.path.join('movie', 'adapters', 'data')
    print(data_path, '#'*10)
    moive_list = []

    for data_row in read_csv_file(os.path.join(data_path, 'news_movies.csv')):
        print(data_row, '#'*5)
        movie_key = int(data_row[0])

        # Create Moive object.
        movie = Movie(
            title=data_row[1],
            # date=date.fromisoformat(data_row[2]),
            release_year=int(data_row[2]),
            # image_hyperlink=data_row[5],
            id=movie_key
        )
        moive_list.append(movie)
    return moive_list


class MemoryRepository(AbstractRepository):
    # Articles ordered by date, not id. id is assumed unique.

    def __init__(self):
        self._movies = list()
        
    def load_movies(self) -> List[Movie]:
        self._movies = load_movies()
        return self._movies

