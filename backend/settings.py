from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "API"
    bind_host: str = "0.0.0.0"
    bind_host_port: int = 80
    token_header_name: str = "header-name"
    token: str = "token"

    # FastAPI defaults
    openapi_url: str = "/openapi.json"
    swagger_ui_oauth2_redirect_url: str = "/docs/oauth2-redirect"

    # Logging
    default_log_format: str = '[{time:%Y-%m-%d %H:%M:%S:%f %z}] - {name} - <level>{level}</level> - {message}'
    log_level: str = 'INFO'

    # Override settings with OS ENV values
    model_config = SettingsConfigDict(env_file=".env")


@lru_cache()
def get_settings():
    return Settings()


settings = get_settings()
