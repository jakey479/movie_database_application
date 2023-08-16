import requests
from requests.models import Response


class OMDBApiHandler:

    def __init__(self):
        self.api_key: str = 'http://www.omdbapi.com/?apikey=66544728&t='

    def return_api_response(self, api_param: str) -> Response:
        """
        return an api response based on a query parameter
        :api_param movie_name:
        :return:
        """
        api_response = requests.get(self.api_key + api_param)
        return api_response

    def convert_api_json_response_to_python_object(self, api_response):
        python_object = api_response.json()
        return python_object


# api_handler = OMDBApiHandler()
# response = api_handler.return_api_response(api_param='Gladiator')
# print(response)
# python_response = api_handler.convert_api_json_response_to_python_object(api_response=response)
# print(python_response)