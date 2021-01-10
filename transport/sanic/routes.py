from transport.sanic.endpoints.health import HealthEndpoint
from typing import Tuple
from configs.config import ApplicationConfig
from transport.sanic.base import SanicEndpoint
from context import Context

def get_routes(config: ApplicationConfig, context: Context) -> Tuple['SanicEndpoint']:
    return(
        HealthEndpoint(config=config, uri='/', methods=['POST','GET'], context=context),
    )