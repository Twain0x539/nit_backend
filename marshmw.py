from marshmallow import Schema, fields, ValidationError, EXCLUDE
from sanic.exceptions import SanicException

class ApiValidationException(SanicException):
    status = 400



class RequestCreateEmployeeDtoSchema(Schema):
    first_name = fields.Str(required=True,allow_none=False)
    last_name = fields.Str(required=True, allow_none=False)



class RequestDto:
    __schema__: Schema

    def __init__(self,data:dict):
        try:
            valid_data = self.__schema__(unknown=EXCLUDE).load(data)
        except ValidationError as error:
            raise ApiValidationException(error.messages)
        else:
            self._import(valid_data)



    def _import(self,data:dict):
        for name, field in data.items():
            self.set(name,field)


    def set(self,key,value):
        setattr(self,key,value)


if __name__ == "__main__":
    body = {"first_name":"mikhail", "last_name":"karaev",'boba':'hleboba'}

    try:
        schema = RequestCreateEmployeeDtoSchema(unknown=EXCLUDE).load(body)
    except ValidationError as err:
        print(err.messages())


    print(schema)