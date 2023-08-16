from class_interfaces.storage import MovieStorageHandler
from validator_class import Validator
from user_interface_class import UserInterface
from api_handler_class import OMDBApiHandler
from utils import print_to_screen, dictionary_formatter
from templates import generate_website
import os


class MovieApp:
    def __init__(
            self,
            storage: MovieStorageHandler,
            validator: Validator,
            user_interface: UserInterface,
            api_handler: OMDBApiHandler,
            database_name: str
    ):
        self.storage = storage
        self.validator = validator
        self.user_interface = user_interface
        self.api_handler = api_handler
        self.database_name = database_name

    def run(self):
        while True:
            print_to_screen.display_menu_page()
            user_input = self.user_interface.return_menu_selection()
            is_valid_user_input = self.validator.value_is_in_valid_inputs(
                value=user_input,
                valid_inputs=['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
            )
            movie_database_list = self.storage.return_list_of_dictionaries_from_file()
            movie_title_movie_ratings_dictionary = dictionary_formatter.map_key_in_list_of_dictionaries_to_new_value(
                list_of_dictionaries=movie_database_list,
                key='Title',
                key_of_new_value='imdbRating'
            )
            # sorted movie title ratings dictionary and list of movie ratings are
            # sorted in ascending order
            sorted_movie_title_ratings_dictionary = dictionary_formatter.sort_dictionary_by_numerical_values(
                dictionary=movie_title_movie_ratings_dictionary
            )
            list_of_movie_ratings = dictionary_formatter.return_values_in_dictionary(
                dictionary=sorted_movie_title_ratings_dictionary
            )
            if not is_valid_user_input:
                print_to_screen.non_valid_input_display()
                continue
            if user_input == '1':
                self.storage.list_movies(movie_database_list=movie_database_list)
                print_to_screen.return_to_menu_page()
                continue
            elif user_input == '2':
                movie_to_add = self.user_interface.return_movie_to_add()
                api_response = self.api_handler.return_api_response(
                    api_param=movie_to_add
                )
                dictionary_response = self.api_handler.convert_api_json_response_to_python_object(
                    api_response=api_response
                )
                if self.validator.false_in_dictionary_values(
                    dictionary=dictionary_response
                ):
                    print_to_screen.print_non_valid_movie_message()
                    print_to_screen.return_to_menu_page()
                    continue
                key_values_from_dict = dictionary_formatter.return_keys_and_values_from_dictionary(
                    dictionary=dictionary_response,
                    list_of_keys=self.storage.fields
                )
                new_movie_dictionary = dictionary_formatter.convert_list_of_key_values_to_dictionary(
                    list_of_key_values=key_values_from_dict
                )
                new_movie_dictionary['My Rating'] = 'N/A'
                self.storage.add_movie(
                    movie_dictionary=new_movie_dictionary,
                    movie_database_list=movie_database_list
                )
                print(f'\n{movie_to_add} successfully added to database')
                print_to_screen.return_to_menu_page()
            elif user_input == '3':
                movie_to_delete = self.user_interface.return_movie_to_delete()
                if not self.validator.key_is_in_list_of_dictionaries(
                        list_of_dictionaries=self.storage.return_list_of_dictionaries_from_file(),
                        key=movie_to_delete
                ):
                    print_to_screen.print_non_valid_movie_message()
                    print_to_screen.return_to_menu_page()
                    continue
                self.storage.delete_movie(
                    title=movie_to_delete,
                    movie_database_list=movie_database_list
                )
                print(f'\n{movie_to_delete} Successfully removed from database')
                print_to_screen.return_to_menu_page()
            elif user_input == '4':
                movie_to_update = self.user_interface.return_movie_to_update()
                if not self.validator.key_is_in_list_of_dictionaries(
                        key=movie_to_update,
                        list_of_dictionaries=self.storage.return_list_of_dictionaries_from_file()
                ):
                    print_to_screen.print_non_valid_movie_message()
                    print_to_screen.return_to_menu_page()
                    continue
                movie_rating_update = self.user_interface.return_movie_rating_update()
                if not self.validator.string_is_numeric(movie_rating_update):
                    print_to_screen.print_non_valid_movie_rating_message()
                    print_to_screen.return_to_menu_page()
                    continue
                self.storage.update_movie(
                    title=movie_to_update,
                    my_rating=movie_rating_update,
                    movie_database_list=movie_database_list
                )
                print(f"\n{movie_to_update} is now rated {movie_rating_update}")
                print_to_screen.return_to_menu_page()
            elif user_input == '5':
                print_to_screen.print_movie_stats(
                    sorted_movie_ratings_dictionary=sorted_movie_title_ratings_dictionary,
                    list_of_movie_ratings=list_of_movie_ratings)
                print_to_screen.return_to_menu_page()
                continue
            elif user_input == '6':
                print_to_screen.print_random_movie(
                    sorted_movie_ratings_dictionary=sorted_movie_title_ratings_dictionary
                )
                print_to_screen.return_to_menu_page()
                continue
            elif user_input == '7':
                print_to_screen.print_movie_from_database(
                    sorted_movie_ratings_dictionary=sorted_movie_title_ratings_dictionary
                )
                print_to_screen.return_to_menu_page()
                continue
            elif user_input == '8':
                print_to_screen.return_ranked_list_of_movies(
                    sorted_movie_ratings_dictionary=sorted_movie_title_ratings_dictionary
                )
                print_to_screen.return_to_menu_page()
                continue
            elif user_input == '9':
                html_template_filepath = os.path.join(
                    'templates',
                    'html_template.html'
                )
                html_template_string = generate_website.read_html_template_to_string(
                    html_template_filepath=html_template_filepath
                )
                html_template_with_database_name_title = generate_website.change_user_template_title(
                    html_template=html_template_string,
                    database_name=self.database_name
                )
                user_database_html = generate_website.generate_html_output_for_movie(
                   movie_database_list=movie_database_list
                )
                movie_database_html_filepath = os.path.join('templates', 'movie_database.html')
                generate_website.generate_website_html(

                    html_template=html_template_with_database_name_title,
                    movie_database_html=user_database_html,
                    movie_database_html_filepath=movie_database_html_filepath
                )
                generate_website.open_html(movie_database_html_filepath)
                print_to_screen.return_to_menu_page()
                continue
            elif user_input == '0':
                print('\nbye!')
                break
