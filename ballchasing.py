from urllib.parse import urljoin
import requests


class Ballchasing:
    BASE_URL = 'https://ballchasing.com/api/'

    def __init__(self, token):
        self.token = token
        self.headers = {'Authorization': self.token}

    def _fetch(self, endpoint='', params=None):
        """Parent method for making GET requests."""
        url = urljoin(self.BASE_URL, endpoint)
        r = requests.get(url, headers=self.headers, params=params)
        r.raise_for_status()
        return r.json()

    def ping(self):
        """Used to check if your API token is correct."""
        return self._fetch()

    def replays(self, params):
        return self._fetch('replays', params)
