"""
Base class sharing common properties and methods that can be reused for all endpoints.
The root url for all Numbeo API requests is https://www.numbeo.com/api/
"""

import os
import json
import requests
from requests.exceptions import ReadTimeout
from typing import Dict


class NumbeoClient:
    """
    Base API properties for all endpoints
    """

    def __init__(self, api_key: str = None):
        """
        :param api_key: api key from numbeo
        """
        self.url = "https://www.numbeo.com/api/"
        self.api_key = api_key

        if api_key is None:
            with open('apikey.json') as f:
                self.api_key = json.load(f)['api_key']

    def request(self, path: str, params: dict = None) -> str:
        """
        API request method
        Args:
            path (str): API resource path
            params (dict): query parameters dictionary for passed-in path
        Returns:
            response (dict): parsed JSON response
        """
        URL = f"{self.url}/{path}"
        params['api_key'] = self.api_key
        response = requests.get(url=URL, params=params)
        return response
