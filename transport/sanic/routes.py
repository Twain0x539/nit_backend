from transport.sanic.endpoints.health import HealthEndpoint
from typing import Tuple
from configs.config import ApplicationConfig
from transport.sanic.base import SanicEndpoint

def get_routes(config: ApplicationConfig) -> Tuple['SanicEndpoint']:
    return(
        HealthEndpoint(config, uri='/', methods=['POST','GET']),
    )