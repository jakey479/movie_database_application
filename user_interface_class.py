class UserInterface:

    def return_menu_selection(self) -> str:
        user_input = input('\nWhich action would you like to perform (0-9): ')
        return user_input

    def return_movie_to_update(self) -> str:
        movie_to_update = input("\nWhich movie would you like to update (Please enter the title as it "
                                "appears in the database): ").title()
        return movie_to_update

    def return_movie_rating_update(self) -> str:
        movie_rating_update = input("\nWhat is the new rating: ")
        return movie_rating_update

    def return_movie_to_delete(self) -> str:
        movie_to_delete = input("\nWhich movie would you like to remove from the database "
                                "(Please enter the full title name): ").title()
        return movie_to_delete

    def return_movie_to_add(self) -> str:
        movie_to_add = input("\nWhich movie would you like to add to the database: ").title()
        return movie_to_add

    def return_database_name(self) -> str:
        database_name = input('\nWhat is the name of the database you would like to work with: ')
        return database_name

    def return_database_type(self) -> str:
        database_type = input('\nPlease type either ".json" or ".csv" to save this file: ')
        return database_type

    def return_either_csv_or_json_string(self) -> str:
        while True:
            string = self.return_database_type()
            if string in ['.csv', '.json']:
                return string
