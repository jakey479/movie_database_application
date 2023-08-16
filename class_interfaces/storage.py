from abc import ABC, abstractmethod


class MovieStorageHandler(ABC):
    filepath: str
    fields: list[str]

    @abstractmethod
    def write_list_of_dictionaries_to_file(self, list_of_dictionaries: list[dict]) -> None:
        pass

    @abstractmethod
    def return_list_of_dictionaries_from_file(self) -> list[dict]:
        pass

    @abstractmethod
    def list_movies(self, movie_database_list: list[dict]) -> None:
        pass

    @abstractmethod
    def add_movie(self, movie_dictionary: dict, movie_database_list: list[dict]) -> None:
        pass

    @abstractmethod
    def delete_movie(self, title: str, movie_database_list: list[dict]) -> None:
        pass

    @abstractmethod
    def update_movie(self, title: str, my_rating: str, movie_database_list: list[dict]) -> None:
        pass
