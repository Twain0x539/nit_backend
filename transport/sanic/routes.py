from typing import Tuple

from context import Context
from configs.config import ApplicationConfig
from transport.sanic.base import SanicEndpoint
from transport.sanic import endpoints

def get_routes(config: ApplicationConfig, context: Context) -> Tuple:
    return(
        endpoints.HealthEndpoint(config=config, uri='/', methods=['POST','GET'], context=context),
        endpoints.CreateEmployeeEndpoint(config,context,uri='/employee',methods=['POST',]),
    )