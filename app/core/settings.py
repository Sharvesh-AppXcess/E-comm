from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # debug: bool = False
    # app_env: str = "development"

    # class config:  # noqa: N801
    #     env_file = ".env"
    #     extra = "ignore"
    debug: bool
    app_env: str
    DB_NAME: str
    DB_USER: str
    DB_PASSWORD: str
    DB_HOST: str 
    DB_PORT: int
    
    # REDIS_PASSWORD: str = ""
    # REDIS_HOST: str = "localhost"
    # REDIS_PORT: int = 6379  
    
    class Config:
        env_file = ".env"
        extra = "ignore"

settings = Settings()
