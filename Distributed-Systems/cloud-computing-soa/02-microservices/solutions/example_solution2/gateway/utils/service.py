from gateway.utils.load_balancer import LoadBalancer
from common_utils.const import AUTH_SERVER_PORTS, URL_SHORTENER_PORTS, PROD_VAR, PROD_VAL
from common_utils.util import get_env_variable

LOCAL_HOST = "127.0.0.1"
SERVICES = {
    "url_shortener_service": "http://{}:{}",
    "auth_service": "http://{}:{}",
}
DEV_SERVERS = {
    "url_shortener_service": LoadBalancer(URL_SHORTENER_PORTS),
    "auth_service": LoadBalancer(AUTH_SERVER_PORTS)
}
PROD_SERVERS = {
    "url_shortener_service": URL_SHORTENER_PORTS[0],
    "auth_service": AUTH_SERVER_PORTS[0]
}

def get_service_url(service):
    production_env = get_env_variable(PROD_VAR)
    if production_env == PROD_VAL:
        server_port = PROD_SERVERS[service]
        server_address = service
    else:
        server_port = DEV_SERVERS[service].round_robin()
        server_address = LOCAL_HOST
    return SERVICES[service].format(server_address, server_port)