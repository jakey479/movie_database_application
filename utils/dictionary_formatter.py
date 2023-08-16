def return_keys_and_values_from_dictionary(
        dictionary: dict,
        list_of_keys: list[str | int]
        ) -> list[list]:
    """
    :param dictionary:
    :param list_of_keys:
    :return:
    """
    key_value_pairings = []
    for key, value in dictionary.items():
        if key in list_of_keys:
            key_value_pairings.append([key, value])
    return key_value_pairings


def convert_list_of_key_values_to_dictionary(list_of_key_values: list[list]) -> dict:
    dictionary = {}
    for key_values in list_of_key_values:
        key = key_values[0]
        value = key_values[1]
        dictionary[key] = value
    return dictionary


def sort_dictionary_by_numerical_values(dictionary: dict) -> dict:
    """
    initializes a dictionary and adds new key value pairs to for each movie and its rating in
    the data file and then uses a lambda function to sort it by its values.
    :return:
    """
    sorted_dictionary_of_movie_ratings = sorted(dictionary.items(), key=lambda kv: kv[1])
    return dict(sorted_dictionary_of_movie_ratings)


def return_values_in_dictionary(dictionary: dict) -> list:
    list_of_values = []
    for value in dictionary.values():
        list_of_values.append(value)
    return list_of_values


def map_key_in_list_of_dictionaries_to_new_value(
        list_of_dictionaries: list[dict],
        key: str | int,
        key_of_new_value: str | int
):
    """
    initializes a dictionary and adds new key value pairs to for each movie and its rating in
    the data file and then uses a lambda function to sort it by its values.
    :return:
    """
    newly_mapped_dictionary = {}
    for dictionary in list_of_dictionaries:
        newly_mapped_dictionary[dictionary[key]] = dictionary[key_of_new_value]
    return newly_mapped_dictionary
