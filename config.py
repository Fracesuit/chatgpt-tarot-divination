import logging

from pydantic import BaseSettings, Field

logging.basicConfig(
    format="%(asctime)s: %(levelname)s: %(name)s: %(message)s",
    level=logging.INFO
)
_logger = logging.getLogger(__name__)


class Settings(BaseSettings):
    api_key: str = Field(default="sk-xxx", exclude=True)
    api_base: str = "https://api.openai.com/v1"
    model: str = "gpt-3.5-turbo"
    rate_limit: str = "70/hour"
    user_rate_limit: str = "700/hour"
    github_client_id: str = Field(default="secret", exclude=True)
    github_client_secret: str = Field(default="", exclude=True)
    jwt_secret: str = Field(default="secret", exclude=True)
    ad_client: str = Field(default="", exclude=True)
    ad_slot: str = Field(default="", exclude=True)

    class Config:
        env_file = ".env"


settings = Settings()
_logger.info(f"settings: {settings.json(indent=2)}")
