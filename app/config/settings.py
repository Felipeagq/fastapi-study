from pydantic import BaseSettings, ValidationError, AnyHttpUrl
from typing import List
import os


class Settings(BaseSettings):
    PROJECT_NAME: str = "Estudio FastAPI"
    PROJECT_VERSION: str = "v0.0.1"
    API_V1_STR: str = "/api/"
    
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = []
    
    _PG_NAME: str = os.getenv("PG_NAME") or None
    _PG_USER: str = os.getenv("PG_USER") or None
    _PG_HOST: str = os.getenv("PG_HOST") or None
    _PG_PORT: str = os.getenv("PG_PORT") or None
    _PG_PASSWORD: str = os.getenv("PG_PASSWORD") or None


settings = Settings()