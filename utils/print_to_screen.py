import random as rand


def return_to_menu_page() -> None:
    confirm_return_to_menu = input("\nPress enter to return to the main page")


def display_welcome_message() -> None:
    print("Welcome to your Movie Database!")


def display_menu_page() -> None:
    """
    Display command options to user
    """
    print("""
0. Exit app

1. List movies

2. Add movie

3. Delete movie

4. Update movie

5. Movie stats

6. Select random movie

7. Search movie

8. Sort movies by rating

9. Generate website""")


def return_menu_selection() -> str:
    menu_selection = input('\nPlease select a menu option from 0-9: ')
    return menu_selection


def print_non_valid_movie_message() -> None:
    print('\nMovie is not available')


def print_non_valid_movie_rating_message() -> None:
    print('\nNot a valid rating')


def non_valid_input_display() -> None:
    print('user input is not valid, please select a valid option from the menu page')


def print_average_movie_rating(list_of_movie_ratings: list[str]) -> None:
    """
    sums a list of dictionary values and calculates their average
    :return:
    """
    sum_of_movies = sum(
        [float(integer) for integer in list_of_movie_ratings]
    )
    number_of_movies = len(list_of_movie_ratings)
    average_movie_ratings = sum_of_movies / number_of_movies
    print(f"\nAverage movie rating is {round(average_movie_ratings, 2)}")


def print_median_movie_rating(list_of_movie_ratings: list, ) -> None:
    """
    sorts a list of movie ratings and then prints out either middle one or middle two ratings
    :return:
    """
    median_index_position = len(list_of_movie_ratings) // 2
    sorted_list_of_movie_ratings = sorted(list_of_movie_ratings)
    if len(list_of_movie_ratings) % 2 == 1:
        print(f"\nMedian movie rating is {sorted_list_of_movie_ratings[median_index_position]}")
    else:
        print(f"\nMedian movie rating are "
              f"{list_of_movie_ratings[median_index_position - 1]} "
              f"and {list_of_movie_ratings[median_index_position]}")


def print_highest_rated_movie(sorted_movie_ratings_dictionary: dict) -> None:
    """
    :return:
    """
    highest_movie_rating = list(sorted_movie_ratings_dictionary.values())[-1]
    print('\nThe highest rated movies are:\n')
    for movie, rating in sorted_movie_ratings_dictionary.items():
        if rating == highest_movie_rating:
            print(f'{movie}: {rating}')


def print_lowest_rated_movie(sorted_movie_ratings_dictionary: dict) -> None:
    lowest_movie_rating = list(sorted_movie_ratings_dictionary.values())[0]
    print('\nThe lowest rated movies are:\n')
    for movie, rating in sorted_movie_ratings_dictionary.items():
        if rating == lowest_movie_rating:
            print(f'{movie}: {rating}')


def print_random_movie(sorted_movie_ratings_dictionary: dict) -> None:
    """
    uses random module to select a random movie from a list converted from a dictionary
    :return:
    """
    random_movie_selection = rand.choice(list(sorted_movie_ratings_dictionary.items()))
    movie = random_movie_selection[0]
    movie_rating = random_movie_selection[1]
    print(f"\nWould you like to watch {movie}? You've previously given it a rating of {movie_rating}")


def print_movie_from_database(sorted_movie_ratings_dictionary: dict) -> None:
    """
    returns a movie from dictionary of movies and ratings based on user input
    :return:
    """
    substring_to_check = input("\nEnter a part of the movie title you would like to look up: ")
    for movie, movie_rating in sorted_movie_ratings_dictionary.items():
        if substring_to_check.title() in movie:
            print(f'{movie} is rated {movie_rating}')


def return_ranked_list_of_movies(sorted_movie_ratings_dictionary: dict) -> None:
    for movie, movie_rating in tuple(sorted_movie_ratings_dictionary.items())[::-1]:
        print('')
        print(f'{movie} is rated {movie_rating}')


def print_movie_stats(sorted_movie_ratings_dictionary: dict, list_of_movie_ratings: list) -> None:
    print_average_movie_rating(list_of_movie_ratings)
    print_median_movie_rating(list_of_movie_ratings)
    print_highest_rated_movie(sorted_movie_ratings_dictionary)
    print_lowest_rated_movie(sorted_movie_ratings_dictionary)