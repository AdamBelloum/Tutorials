import os
from common_utils.const import PROD_VAL, PROD_VAR


def get_env_variable(var_name):
    try:
        return os.environ[var_name]
    except KeyError:
        print(f'The environment variable {var_name} is not set, returning None.')
        return None
    
def get_auth_service_host():
    production_env = get_env_variable(PROD_VAR)
    if production_env == PROD_VAL:
        return "http://auth_service:8001"
    
    return "http://127.0.0.1:8001"