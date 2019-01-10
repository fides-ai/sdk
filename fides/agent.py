import datetime
import requests
from fides.config import Config


DEFAULT_PROPERTIES_FILE_NAME = 'fides.ini'
ENV_FIDES_PROPERTIES_FILE = 'FIDES_PROPERTIES_FILE'
PROP_FIDES_SERVER_URL_NAME = 'FIDES_SERVER_URL'
PROP_FIDES_SERVER_URL_VAL = 'localhost'
PATH_AGENT_CONNECT = 'api/agent/connect'
PATH_AGENT_PING = 'api/agent/ping'
PATH_INFERENCE = 'api/inference'


class Agent(object):

    def __init__(self, connect=True):
        if connect:
            self.connect()

    def connect(self):
        data = {}
        self._send(data, path=PATH_AGENT_CONNECT)

    def send_inference(self, data):
        self._send(data, path=PATH_INFERENCE)

    def _send(self, data, path=''):
        """
        """
        base_data = self._get_base_data()
        data = {**base_data, **data}
        base_url = Config.get_property('PROP_FIDES_SERVER_URL_NAME', default=PROP_FIDES_SERVER_URL_VAL)
        url = '/'.join(base_url, path)
        requests.post(url, data=data)

    def _get_base_data(self):
        """
        """
        base_data = {
            'timestamp': datetime.datetime.now()
        }
        base_data = {**base_data, **self.credentials}
        return base_data

