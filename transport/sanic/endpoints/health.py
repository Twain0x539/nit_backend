from sanic.request import Request
from sanic.response import HTTPResponse,json

async def health_endpoint(request: Request) -> HTTPResponse:
    responce = {
        'name': 'mikhail',
        'surname': 'na_babkah'
    }

    if request.method == "POST":
        responce.update(request.json)

    return json(body=responce, status=200)