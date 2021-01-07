from sanic.request import Request
from sanic.response import HTTPResponse,json
from transport.sanic.base import SanicEndpoint

class HealthEndpoint(SanicEndpoint):
    async def method_get(self, request: Request, body: dict, *args, **kwargs):
        responce = {
            'hello':'world'
        }
        return await self.make_responce_json(body=responce,status=200)

    async def method_post(self,request: Request, body:dict, *args, **kwargs):
        return await self.make_responce_json(body=body,status=200)