from class_interfaces.storage import MovieStorageHandler
import json


class JsonMovieStorageHandler(MovieStorageHandler):

    def __init__(self, filepath: str, fields: list[str]):
        self.filepath = filepath
        self.fields = fields

    def write_list_of_dictionaries_to_file(self, list_of_dictionaries: list[dict]) -> None:
        """
        write to a json file by appending a movie dictionary to a python object and then writing over the
        pre-existing json file
        :param list_of_dictionaries:
        :return:
        """
        with open(self.filepath, 'w') as fileobj:
            json.dump(list_of_dictionaries, fileobj, indent=4)

    def return_list_of_dictionaries_from_file(self) -> list[dict]:
        """
        parse json object from file and return python representation
        :return:
        """
        with open(self.filepath) as fileobj:
            python_data_object = json.load(fileobj)
            return python_data_object

    def list_movies(self, movie_database_list: list[dict]) -> None:
        """
        access current json movie data and print out each one along with its info
        :return:
        """
        movie_database_list = self.return_list_of_dictionaries_from_file()
        print(f"\ntotal movies: {len(movie_database_list)}\n")
        for movie in movie_database_list:
            for movie_key, movie_value in movie.items():
                print(f'{movie_key}: {movie_value}')
            print('')

    def add_movie(self, movie_dictionary: dict, movie_database_list: list[dict]) -> None:
        """
        store python representation of json api data in a variable and attempts to initialize
        variables which hold dictionary key value pairs representing specific movie data. Either
        appends movie info dictionary to json database or handles it based on api response
        :return:
        """
        movie_database_list.append(movie_dictionary)
        self.write_list_of_dictionaries_to_file(list_of_dictionaries=movie_database_list)

    def delete_movie(self, title: str, movie_database_list: list[dict]) -> None:
        """
        uses enumerate function to be able to delete movie based on index position if movie
        found in database
        :return:
        """
        movie_database_list = self.return_list_of_dictionaries_from_file()
        for index, movie_dictionary in enumerate(movie_database_list):
            movie_title = str(movie_dictionary["Title"]).title()
            if title in movie_title:
                del movie_database_list[index]
                self.write_list_of_dictionaries_to_file(
                    list_of_dictionaries=movie_database_list
                )

    def update_movie(self, title: str, my_rating: int, movie_database_list: list[dict]) -> None:
        movie_database_list = self.return_list_of_dictionaries_from_file()
        for movie in movie_database_list:
            if title == str(movie["Title"]).title():
                movie['My Rating'] = my_rating
                self.write_list_of_dictionaries_to_file(
                    list_of_dictionaries=movie_database_list
                )
