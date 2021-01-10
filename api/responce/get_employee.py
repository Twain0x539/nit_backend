from marshmallow import Schema, fields

from api.base import ResponceDto

class ResponceGetEmployeeDtoSchema(Schema):
    eid = fields.Int(required=True, allow_none=False)


class ResponceGetEmployeeDto(ResponceDto):
    __schema__ = ResponceGetEmployeeDtoSchema