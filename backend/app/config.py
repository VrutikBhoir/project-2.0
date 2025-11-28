from pydantic import BaseSettings
from functools import lru_cache


class Settings(BaseSettings):
    # ───────────────────────────────
    # APP CONFIGURATION
    # ───────────────────────────────
    APP_NAME: str = "Stock Price Prediction API"
    APP_VERSION: str = "1.0.0"
    ENVIRONMENT: str = "development"   # development / production

    # ───────────────────────────────
    # MODEL PATHS
    # ───────────────────────────────
    LSTM_MODEL_PATH: str = "app/models/lstm_model.h5"
    ARIMA_MODEL_PATH: str = "app/models/arima_model.pkl"
    SARIMA_MODEL_PATH: str = "app/models/sarima_model.pkl"
    LIGHTGBM_MODEL_PATH: str = "app/models/lightgbm_model.txt"
    SCALER_PATH: str = "app/models/scaler.pkl"

    # ───────────────────────────────
    # DATA SETTINGS
    # ───────────────────────────────
    REALTIME_CACHE_PATH: str = "data/realtime_cache.json"

    # ───────────────────────────────
    # EXTERNAL APIs (Optional)
    # ───────────────────────────────
    YFINANCE_ENABLED: bool = True

    # ───────────────────────────────
    # SECURITY & CORS
    # ───────────────────────────────
    ALLOWED_ORIGINS: str = "*"   # you can restrict in prod

    class Config:
        env_file = ".env"   # Load variables from .env file
        case_sensitive = True


# ───────────────────────────────
# Cached settings loader
# ───────────────────────────────
@lru_cache()
def get_settings():
    return Settings()
