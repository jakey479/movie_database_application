from validator_class import Validator
from csv_movie_storage_handler_class import CsvMovieStorageHandler
from json_movie_storage_handler_class import JsonMovieStorageHandler
from user_interface_class import UserInterface
from api_handler_class import OMDBApiHandler
from movie_app_class import MovieApp
import os
import csv
import json


def main():
    fields = ['Title', 'Year', 'Poster', 'Actors', 'Plot', 'imdbRating', 'Director', 'My Rating']
    user_interface = UserInterface()
    validator = Validator(
    )
    api_handler = OMDBApiHandler()
    user_database_name = user_interface.return_database_name()
    user_database_type = user_interface.return_either_csv_or_json_string()
    if user_database_type == '.csv':
        user_database_filepath = (
            os.path.join('data', user_database_name) + user_database_type
        )
        if not validator.file_exists(filepath=user_database_filepath):
            with open(user_database_filepath, 'w', newline='') as fileobj:
                csv_writer = csv.DictWriter(fileobj, fieldnames=fields)
                csv_writer.writeheader()
        csv_movie_storage_handler = CsvMovieStorageHandler(
            filepath=user_database_filepath,
            fields=fields
        )
        app = MovieApp(
            storage=csv_movie_storage_handler,
            validator=validator,
            user_interface=user_interface,
            api_handler=api_handler,
            database_name=user_database_name
        )
        app.run()
    if user_database_type == '.json':
        user_database_filepath = (
            os.path.join('data', user_database_name) + user_database_type
        )
        if not validator.file_exists(filepath=user_database_filepath):
            with open(user_database_filepath, 'w') as fileobj:
                json.dump([], fileobj)
        json_movie_storage_handler = JsonMovieStorageHandler(
            filepath=user_database_filepath,
            fields=fields
        )
        app = MovieApp(
            storage=json_movie_storage_handler,
            validator=validator,
            user_interface=user_interface,
            api_handler=api_handler,
            database_name=user_database_name
        )
        app.run()


if __name__ == '__main__':
    main()
