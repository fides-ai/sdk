from fides.agent import Agent
from fides.model import Model

DEFAULT_PROPERTIES_FILE_NAME = 'fides.ini'
ENV_FIDES_PROPERTIES_FILE = 'FIDES_PROPERTIES_FILE'
PROP_FIDES_SERVER_URL_NAME = 'FIDES_SERVER_URL'
PROP_FIDES_SERVER_URL_VAL = 'localhost'
PATH_CONNECT = 'api/agent/connect'
PATH_PING = 'api/agent/ping'


class Client(object):

    def __init__(self, credentials, connect=True):
        self.credentials = credentials
        self.agent = Agent(connect)
        self.models = []

    def bind(self,
             model_id):
        model = Model(model_id)
        model.bind()
        self.models[model_id] = model

    def explain(self,
                model_id,
                x,
                y):
        model = self.models[model_id]

        if not model:
            return False

        data = model.track_prediction(x)
        self.agent.send_inference(data)

        return True
