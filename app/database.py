from pydantic_settings import BaseSettings

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker


class DBSettings(BaseSettings):

    db_name: str
    db_user: str
    db_password: str
    db_host: str = "localhost"
    db_port: int = 5432

    class Config:
        env_file = ".env"
        extra = "ignore"


settings = DBSettings()


DATABASE_URL = (
    f"postgresql://"
    f"{settings.db_user}:"
    f"{settings.db_password}@"
    f"{settings.db_host}:"
    f"{settings.db_port}/"
    f"{settings.db_name}"
)


engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()