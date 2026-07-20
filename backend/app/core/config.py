from decouple import config


class Settings:
    DATABASE_HOST = config("DATABASE_HOST")
    DATABASE_PORT = config("DATABASE_PORT")
    DATABASE_NAME = config("DATABASE_NAME")
    DATABASE_USER = config("DATABASE_USER")
    DATABASE_PASSWORD = config("DATABASE_PASSWORD")

    SECRET_KEY = config("SECRET_KEY")
    ALGORITHM = config("ALGORITHM")
    ACCESS_TOKEN_EXPIRE_MINUTES = config(
        "ACCESS_TOKEN_EXPIRE_MINUTES", cast=int
    )


settings = Settings()
