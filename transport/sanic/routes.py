from transport.sanic.endpoints.health import health_endpoint
from configs.config import ApplicationConfig

def get_routes(config: ApplicationConfig):
    return(
        (health_endpoint, '/', ['POST','GET']),
    )