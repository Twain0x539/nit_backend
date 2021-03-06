from configs.config import ApplicationConfig
from sanic.response import BaseHTTPResponse,json
from sanic.request import Request
from http import HTTPStatus
from context import Context
from collections import Iterable

class SanicEndpoint:

    async def __call__(self, *args, **kwargs):
        return await self.handler(*args,**kwargs)

    def __init__(self, config : ApplicationConfig, context: Context, uri:str, methods:Iterable,*args,**kwargs):
        self.config = config
        self.methods = methods
        self.config = config
        self.uri = uri
        self.context = context
        self.__name__ = self.__class__.__name__

    @staticmethod
    async def make_responce_json(body: dict = None, status: int = 200, message: str = None, error_code: int = None
                           ) -> BaseHTTPResponse:

        if body is None:
            body = {
                'message':message or HTTPStatus(status).phrase,
                'error_code':error_code or status
            }

        return json(body=body,status=status)

    @staticmethod
    def import_body_json(request: Request) -> dict:
        if 'application/json' in request.content_type and request.json is not None:
            return dict(request.json)
        return {}


    @staticmethod
    def import_body_headers(request:Request) ->dict:
        return {
            header: value
            for header, value in request.headers.items()
            if header.lower().startswith('x-')
        }


    async def handler(self,request:Request,*args,**kwargs) -> BaseHTTPResponse:
        body = {}

        body.update(self.import_body_json(request))
        body.update(self.import_body_headers(request))

        return await self._method(request,body,*args,**kwargs)

    async def _method(self, request:Request , body: dict, *args, **kwargs) -> BaseHTTPResponse:
        method = request.method.lower()
        func_name = f'method_{method}'
        if hasattr(self,func_name):
            func = getattr(self,func_name)
            return await func(request,body,*args,**kwargs)
        return self.method_not_impl(method=method.upper())



    async def  method_not_impl(self,method: str):
        return await self.make_responce_json(status=500,message=f'Method {method.upper()} not implemented!')

    async def method_get(self, request: Request, body: dict, *args , **kwargs ) -> BaseHTTPResponse:
        return await self.method_not_impl(method='GET')

    async def method_post(self, request: Request, body: dict, *args , **kwargs ) -> BaseHTTPResponse:
        return await self.method_not_impl(method='POST')

    async def method_patch(self, request: Request, body: dict, *args , **kwargs ) -> BaseHTTPResponse:
        return await self.method_not_impl(method='PATCH')

    async def method_delete(self, request: Request, body: dict, *args , **kwargs ) -> BaseHTTPResponse:
        return await self.method_not_impl(method='DELETE')

