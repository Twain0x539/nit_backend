from sqlalchemy import create_engine
from context import Context
from db.database import DataBase
from configs.config import ApplicationConfig

def init_db_sqlite(config:ApplicationConfig, context: Context):
    engine = create_engine(
        config.database.url,
        pool_pre_ping =True,
    )
    database = DataBase(connection=engine)
    database.check_connection()

    context.set('database', database)