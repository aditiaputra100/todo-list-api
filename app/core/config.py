from dotenv import load_dotenv
from pathlib import Path
import os

dev_mode = True if "dev" in os.getenv("ENVIRONMENT", "dev") == "dev" else False
env_path = Path(__file__).resolve().parent.parent.parent / ".env.development" if dev_mode else Path(__file__).resolve().parent.parent.parent / ".env.production"
load_dotenv(dotenv_path=env_path)

class Settings:
    APP_NAME = "Todo List API"
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")
    JWT_ALGORITHM = os.getenv("JWT_ALGORITHM")
    ACCESS_TOKEN_EXPIRE_MINUTES = 30
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "mariadb+mariadbconnector://root@127.0.0.0:3306/todo_list_dev")