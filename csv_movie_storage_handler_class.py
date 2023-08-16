from class_interfaces.storage import MovieStorageHandler
import csv


class CsvMovieStorageHandler(MovieStorageHandler):

    def __init__(self, filepath: str, fields: list):
        self.filepath = filepath
        self.fields = fields

    def write_list_of_dictionaries_to_file(self, list_of_dictionaries: list[dict]) -> None:
        with open(self.filepath, 'w', newline='') as fileobj:
            csv_writer = csv.DictWriter(fileobj, fieldnames=self.fields)
            csv_writer.writeheader()
            for dictionary in list_of_dictionaries:
                csv_writer.writerow(dictionary)

    def return_list_of_dictionaries_from_file(self) -> list[dict]:
        list_of_dictionaries = []
        with open(self.filepath, 'r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                list_of_dictionaries.append(row)
        return list_of_dictionaries

    def list_movies(self, movie_database_list: list[dict]) -> None:
        movie_database_list = self.return_list_of_dictionaries_from_file()
        print(f"\ntotal movies: {len(movie_database_list)}\n")
        for movie in movie_database_list:
            for movie_key, movie_value in movie.items():
                print(f'{movie_key}: {movie_value}')
            print('')

    def add_movie(self, movie_dictionary: dict, movie_database_list: list[dict]) -> None:
        movie_database_list.append(movie_dictionary)
        self.write_list_of_dictionaries_to_file(
            list_of_dictionaries=movie_database_list
        )

    def delete_movie(self, title, movie_database_list: list[dict]) -> None:
        movie_database_list = movie_database_list
        for index, movie_dictionary in enumerate(movie_database_list):
            movie_title = str(movie_dictionary["Title"]).title()
            if title == movie_title:
                del movie_database_list[index]
        self.write_list_of_dictionaries_to_file(
            list_of_dictionaries=movie_database_list
        )

    def update_movie(self, title: str, my_rating: float, movie_database_list: list[dict]) -> None:
        for movie in movie_database_list:
            if title == str(movie["Title"]).title():
                movie['My Rating'] = my_rating
        self.write_list_of_dictionaries_to_file(
            list_of_dictionaries=movie_database_list
        )
