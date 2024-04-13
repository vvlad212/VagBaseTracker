from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    bot_token: str
    tracker_token: str
    tracker_org_id: str

    class Config:
        env_file = '../.env'
        env_file_encoding = 'utf-8'


config = Settings()
