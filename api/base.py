from marshmallow import Schema, fields, ValidationError, EXCLUDE
from sanic.exceptions import SanicException

class ApiValidationException(SanicException):
    status = 400

class ApiResponceValidationException(SanicException):
    status = 500


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


class ResponceDto:
    __schema__: Schema

    def __init__(self, obj: object):
            #properties = {}
            #for prop in dir(obj):
            #    if not prop.startswith('_') and not prop.endswith('_'):
            #        attr = getattr(obj,prop)
            #       if not callable(attr):
            #           valid_data[prop] = attr

        properties = {
            prop:value
            for prop in dir(obj)
            if not prop.startswith('_')
               and not prop.endswith('_')
               and not callable(value := getattr(obj,prop))
        }

        try:
            self._data = self.__schema__(unknown=EXCLUDE).load(properties)
        except ValidationError as error:
            raise ApiValidationException(error.messages)

    def dump(self) -> dict:
        return self._data