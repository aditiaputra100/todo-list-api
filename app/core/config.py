import os

class Settings:
    APP_NAME = "Todo List API"
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")
    JWT_ALGORITHM = os.getenv("JWT_ALGORITHM")
    ACCESS_TOKEN_EXPIRE_MINUTES = 30
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "mariadb+mariadbconnector://root@127.0.0.0:3306/todo_list_dev")