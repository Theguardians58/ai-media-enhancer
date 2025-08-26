```py
import os
from pydantic import BaseModel


class Settings(BaseModel):
SECRET_KEY: str = os.getenv("SECRET_KEY", "change-me")
ALLOWED_ORIGINS: str = os.getenv("ALLOWED_ORIGINS", "*")
TEMP_DIR: str = os.getenv("TEMP_DIR", "/data/tmp")
RESULTS_DIR: str = os.getenv("RESULTS_DIR", "/data/results")
REDIS_URL: str = os.getenv("REDIS_URL", "redis://localhost:6379/0")
BROKER_URL: str = os.getenv("BROKER_URL", "redis://localhost:6379/1")
RESULT_BACKEND: str = os.getenv("RESULT_BACKEND", "redis://localhost:6379/2")
CLEANUP_TTL_SECONDS: int = int(os.getenv("CLEANUP_TTL_SECONDS", "86400"))
REAL_ESRGAN_MODEL: str = os.getenv("REAL_ESRGAN_MODEL", "RealESRGAN_x4plus")
REAL_ESRGAN_TILE: int = int(os.getenv("REAL_ESRGAN_TILE", "0"))
REAL_ESRGAN_FP16: bool = os.getenv("REAL_ESRGAN_FP16", "true").lower()=="true"


settings = Settings()
```
