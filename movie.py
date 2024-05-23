import os
import json
import logging

cur_dir = os.path.dirname(__file__)
data_file = os.path.join(cur_dir, "data", "movies.json")

def get_movies():
    with open(data_file, "r") as f:
        movies_title = json.load(f)
    movies = [Movie(movie_title) for movie_title in movies_title]
    return movies

class Movie:
    def __init__(self, title):
        self.title = title.title()
    
    def __str__(self):
        return f"{self.title}"
    
    def _get_movies(self):
        with open(data_file, "r") as f:
            return json.load(f)

    def _write_movies(self, movies):
        with open(data_file, "w") as f:
            json.dump(movies,f, indent=4, ensure_ascii=False)

    def add_to_movies(self):
        movies = self._get_movies()

        if self.title not in movies:
            movies.append(self.title)
            self._write_movies(movies)
            return True
        else:
            logging.warning(f"Le film {self.title} est déjà enregistré")
            return False
    
    def remove_from_movies(self):
        movies = self._get_movies()

        if self.title in movies:
            movies.remove(self.title)
            self._write_movies(movies)
            return True
        else:
            logging.warning(f"Le film {self.title} n'est pas dans la liste")
            return False
    
if __name__ == "__main__":
    #m = Movie("Harry Potter")
    #m.remove_from_movies()
    movies = get_movies()
    print(movies)
