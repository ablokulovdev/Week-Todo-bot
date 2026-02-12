from decouple import config

class Config():
    NAME = config("DB_NAME")
    USER = config("DB_USER")
    PASS = config("DB_PASS")
    PORT = config("DB_PORT")
    HOST = config("DB_HOST")
    TOKEN = config("BOT_TOKEN")


core = Config()


