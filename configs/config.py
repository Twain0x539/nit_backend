from transport.sanic.config import SanicConfig
from db.config import SQLiteConfig

class ApplicationConfig:
    sanic: SanicConfig
    dataBase: SQLiteConfig
    def __init__(self):
        self.database = SQLiteConfig()
        self.sanic = SanicConfig()