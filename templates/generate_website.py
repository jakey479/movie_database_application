import os
import sys
import webbrowser


def read_html_template_to_string(html_template_filepath: str) -> str:
    """
    parse the html template file and convert it to a python string for later manipulation
    :return:html template as a string
    """
    with open(html_template_filepath) as fileobj:
        html_string = fileobj.read()
        return html_string


def change_user_template_title(html_template: str, database_name: str) -> str:
    """
    stores html string in a variable and replaces the html title with another name
    :return: html template string with updated title
    """
    new_html = html_template.replace('__TEMPLATE_TITLE__', database_name)
    return new_html


def generate_html_output_for_movie(movie_database_list: list) -> str:
    """
    creates an html string that that includes all the html for the movies currently in
    the movie database file
    :return: movie database html string
    """
    html_output = ''
    for movie in movie_database_list:
        html_output += '\n<li>\n<div class = "movie">\n'
        # for movie_name, movie_info in movie.items():
        movie_img = movie["Poster"]
        movie_name = movie["Title"]
        movie_year = movie['Year']
        movie_plot = movie["Plot"]
        movie_director = movie["Director"]
        movie_actors = movie["Actors"]
        html_output += f'<img class = "movie-poster" src = "{movie_img}" title>\n'
        html_output += f'<div class = "movie-title">{movie_name}</div>\n'
        html_output += f'<div class = "movie-year">{movie_year}</div>\n'
        html_output += f'<div class = "movie-plot">{movie_plot}</div>\n'
        html_output += f'<div class = "movie-directors">{movie_director}</div>\n'
        html_output += f'<div class = "movie-actors">{movie_actors}</div>\n'
        html_output += '</div>\n'
        html_output += '</li>'
    return html_output


def generate_website_html(html_template, movie_database_html, movie_database_html_filepath):
    """
    creates a new file that stores the updates html from the html template file
    :return:
    """
    movie_database_html_string = html_template.replace('__TEMPLATE_MOVIE_GRID__', movie_database_html)
    with open(movie_database_html_filepath, 'w') as fileobj:
        fileobj.write(movie_database_html_string)


def open_html(movie_database_html_filepath):
    """
    opens the html file for the updated movie site
    :return:
    """
    webbrowser.open(movie_database_html_filepath)
    print('\nWebsite Generated!')


