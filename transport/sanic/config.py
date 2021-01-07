import os
from dotenv import load_dotenv

load_dotenv()

class SanicConfig:
    host = os.getenv('host','localhost')
    port = int(os.getenv('port'))
    debug = bool(os.getenv('debug'))
    workers = int(os.getenv('workers'))