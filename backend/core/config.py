import os
from dotenv import load_dotenv

from pathlib import Path
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

class Settings:
    PROJECT_NAME : str = 'My App'
    PROJECT_VERSION : str = '1.0.0'

    MYSQL_USER : str = os.getenv("MYSQL_USER")
    MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD")
    MYSQL_SERVER : str = os.getenv("MYSQL_SERVER","localhost")
    MYSQL_PORT : str = os.getenv("MYSQL_PORT",3306) # default mysql port is 3306
    MYSQL_DB : str = os.getenv("MYSQL_DB","test")
    DATABASE_URL = f"mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_SERVER}:{MYSQL_PORT}/{MYSQL_DB}"
    ACCESS_TOKEN_EXPIRE_MINUTES : int = 30
    SECRET_KEY :str = os.getenv("SECRET_KEY")
    ALGORITHM = "HS256"
    TEST_USER_EMAIL = "test@example.com"

settings = Settings()
