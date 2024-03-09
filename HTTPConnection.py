import requests
import constants as const
import logger as log


class HTTPConnection:
    def __init__(self):
        self.base_url = const.BASE_URL

    def send_request(self, **kwargs):
        """Send GET request to https://api.nasa.gov/EPIC endpoint
        Example url: https://api.nasa.gov/EPIC/api/natural/date/2019-05-30?api_key=DEMO_KEY
        EPIC = endpoint
        natural = param
        date = sub_param
        2019-05-30 = value
        """

        url = f"{self.base_url}/EPIC/api/{kwargs.get('param')}/{kwargs.get('sub_param')}/{kwargs.get('value')}?api_key={const.API_KEY}"
        log.logger.info(f"URL: {self.mask_api_key(url)}")
        response = requests.request("GET", url)
        log.logger.debug(response.text)
        return response

    def mask_api_key(self, url):
        """Mask the API key in the URL"""
        api_key_index = url.find(const.API_KEY)
        masked_url = url[:api_key_index] + "*********"  # Replace API key with asterisks
        return masked_url

    def parse_response(self, response):
        try:
            data = response.json()
            return data
        except ValueError:
            return "Failed to parse response"
