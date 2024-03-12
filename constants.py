import os
import logger as log


def get_env_var(env_var):
    try:
        return os.environ.get(env_var)
    except KeyError:
        log.logger.error(f"{env_var} environment variable not found.")
        return None


BASE_URL = "https://api.nasa.gov"
API_KEY = get_env_var('API_KEY')
