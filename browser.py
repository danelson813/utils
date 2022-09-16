import requests
from logger import setup_logger
logger = setup_logger(__name__)


class Browser:

    def __init__(self):
        self.session = requests.session()

    def get(self, url, headers=None, verbose=0):
        headers = headers or {}
        if verbose >= 2:
            logger.info(f"Browser GET Request: {url} (headers={headers})")

        response = self.session.get(url, headers=headers)

        if verbose >= 1:
            logger.info((
                f"Browser GET Response: {url} (headers={headers})"
                f" Status Code {response.status_code} Content {response.content}"
            ))
        return response

    def post(self, url, data=None, headers=None, verbose=0):
        headers = headers or {}
        if verbose >= 2:
            print(f"Browser POST Request: {url} (headers={headers} data={data})")

        response = self.session.post(url, data=data, headers=headers)

        if verbose >= 1:
            logger.info((
                f"Browser POST Response: {url} (headers={headers} data={data})"
                f" Status Code {response.status_code} Content {response.content}"
            ))
        return response
