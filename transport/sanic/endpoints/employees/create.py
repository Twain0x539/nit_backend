from sanic.request import Request
from sanic.response import BaseHTTPResponse

from transport.sanic.endpoints import BaseEndpoint
from api.request import RequestCreateEmployeeDto
from api.response import ResponseEmployeeDto

from db.queries import employee as employee_queries

class CreateEmployeeEndpoint(BaseEndpoint):

    async def method_post(self, request: Request, body: dict, session, *args, **kwargs) -> BaseHTTPResponse:


        request_model = RequestCreateEmployeeDto(body)

        db_employee = employee_queries.create_employee(session, request_model)
        session.commit_session()

        responce_model = ResponseEmployeeDto(db_employee)

        return await self.make_responce_json(body=responce_model.dump(),status=201)
