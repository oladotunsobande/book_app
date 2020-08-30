from dotenv import load_dotenv
from pathlib import Path
import os

env_path = Path('.') / '.env'
load_dotenv(env_path)

MYSQL_URI = os.getenv('MYSQL_URI')
WORK_ENV = os.getenv('WORK_ENV')