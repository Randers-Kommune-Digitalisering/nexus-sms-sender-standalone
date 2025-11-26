import base64
import logging
import requests

logger = logging.getLogger(__name__)


class APIClient:
    def __init__(self, base_url, username=None, password=None):
        self.base_url = base_url
        self.username = username
        self.password = password

    def _authenticate(self):
        try:
            if self.username and self.password:
                auth_str = f"{self.username}:{self.password}"
                b64_auth_str = base64.b64encode(auth_str.encode()).decode()
                auth_header = {'Authorization': f'Basic {b64_auth_str}'}
                return auth_header
            else:
                return {}
        except Exception as e:
            logger.error(e)
            return {}

    def make_request(self, **kwargs):
        if 'path' in kwargs:
            if not isinstance(kwargs['path'], str) and not kwargs['path'] is None:
                raise ValueError('Path must be a string')

        if 'path' in kwargs:
            url = self.base_url.rstrip('/') + '/' + kwargs.pop('path').lstrip('/')
        else:
            url = self.base_url

        if 'headers' in kwargs:
            if not isinstance(kwargs['headers'], dict):
                raise ValueError('Headers must be a dictionary')
            kwargs['headers'] = kwargs['headers'] | self._authenticate()
        else:
            kwargs['headers'] = self._authenticate()

        if not any(ele in kwargs for ele in ['method', 'json', 'data', 'files']):
            method = requests.get
        elif 'method' in kwargs:
            method = getattr(requests, kwargs['method'].lower())
        else:
            method = requests.post

        kwargs.pop('method', None)

        if 'json' in kwargs:
            kwargs['headers']['Content-Type'] = 'application/json'

        return method(url, **kwargs)
