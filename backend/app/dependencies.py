from fastapi import Depends
from .config import get_settings, Settings
from .services.model_handler import ModelHandler

# ─────────────────────────────────────────────
# SETTINGS DEPENDENCY
# Loads configuration via get_settings()
# ─────────────────────────────────────────────
def get_app_settings() -> Settings:
    return get_settings()


# ─────────────────────────────────────────────
# MODEL HANDLER DEPENDENCY
# Loads ML models (LSTM, ARIMA, SARIMA, LightGBM)
# and can be injected into routers
# ─────────────────────────────────────────────
def get_model_handler(
    settings: Settings = Depends(get_app_settings)
):
    return ModelHandler(settings)


# ─────────────────────────────────────────────
# FUTURE-READY: DATABASE / CACHE DEPENDENCIES
# If you add MongoDB / PostgreSQL later,
# you can plug them in here easily.
# ─────────────────────────────────────────────

def get_db():
    """
    Placeholder for a database session dependency.
    Replace with real DB connection if needed.
    """
    return None


def get_cache():
    """
    Placeholder for Redis / in-memory cache dependency.
    """
    return None
