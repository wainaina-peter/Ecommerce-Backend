from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # Database Config
    db_username: str = "postgres"
    db_password: str = "peter"
    db_hostname: str = "localhost"
    db_port: str = "5432"
    db_name: str = "ShopWebsite"

    # JWT Config
    secret_key: str = "OuuU-eKSmsDsXb3pj07Sr8SLxgydSjPs4SO9h0UGTEM"
    algorithm: str = "prefer"
    access_token_expire_minutes: int = 60

    class Config:
        env_file = ".env"


settings = Settings()

