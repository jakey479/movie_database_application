import os


class Validator:

    def value_is_in_valid_inputs(self, value, valid_inputs: list) -> bool:
        if value in valid_inputs:
            return True
        return False

    def key_is_in_list_of_dictionaries(self, key: str, list_of_dictionaries: list[dict]) -> bool:
        for movie in list_of_dictionaries:
            if str(movie["Title"]).title() == key:
                return True
        return False

    def file_exists(self, filepath: str) -> bool:
        return os.path.isfile(filepath)

    def string_is_numeric(self, string: str) -> bool:
        if string.replace(".", "").isnumeric():
            return True
        return False

    def filepath_is_csv_or_json(self, filepath: str):
        if filepath.endswith('.json') or filepath.endswith('.csv'):
            return True
        return False

    def false_in_dictionary_values(self, dictionary: dict) -> bool:
        """
        validate whether one of the values in the movie dictionary is equal to False (will only happen if
        the movie is not found in the database)
        :param dictionary:
        :return:
        """
        if 'False' in dictionary.values():
            return True
        return False




