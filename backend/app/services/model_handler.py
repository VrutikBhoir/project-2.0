import os
import joblib
import numpy as np
import tensorflow as tf
from statsmodels.tsa.statespace.sarimax import SARIMAXResults
from pydantic import BaseModel
from app.config import Settings


class ModelHandler:
    """
    Centralized loader for all prediction models:
    - LSTM
    - ARIMA
    - SARIMA
    - LightGBM
    """

    def __init__(self, settings: Settings):
        self.settings = settings
        self.model_dir = os.path.join(settings.BASE_DIR, "app", "models")

        # Model placeholders
        self.lstm_model = None
        self.arima_model = None
        self.sarima_model = None
        self.lightgbm_model = None
        self.scaler = None

        # Load models at startup
        self.load_all_models()

    # ────────────────────────────────────────────────
    # LOAD ALL MODELS
    # ────────────────────────────────────────────────
    def load_all_models(self):
        self.lstm_model = self._load_lstm()
        self.arima_model = self._load_arima()
        self.sarima_model = self._load_sarima()
        self.lightgbm_model = self._load_lightgbm()
        self.scaler = self._load_scaler()

    # ────────────────────────────────────────────────
    # INDIVIDUAL LOADERS
    # ────────────────────────────────────────────────
    def _load_lstm(self):
        try:
            path = os.path.join(self.model_dir, "lstm_model.h5")
            if os.path.exists(path):
                return tf.keras.models.load_model(path)
        except:
            return None
        return None

    def _load_arima(self):
        try:
            path = os.path.join(self.model_dir, "arima_model.pkl")
            if os.path.exists(path):
                return joblib.load(path)
        except:
            return None
        return None

    def _load_sarima(self):
        try:
            path = os.path.join(self.model_dir, "sarima_model.pkl")
            if os.path.exists(path):
                return SARIMAXResults.load(path)
        except:
            return None
        return None

    def _load_lightgbm(self):
        try:
            path = os.path.join(self.model_dir, "lightgbm_model.txt")
            if os.path.exists(path):
                import lightgbm as lgb
                return lgb.Booster(model_file=path)
        except:
            return None
        return None

    def _load_scaler(self):
        try:
            path = os.path.join(self.model_dir, "scaler.pkl")
            if os.path.exists(path):
                return joblib.load(path)
        except:
            return None
        return None

    # ────────────────────────────────────────────────
    # LSTM PREDICTION
    # ────────────────────────────────────────────────
    def predict_lstm(self, sequence):
        if self.lstm_model is None:
            raise RuntimeError("LSTM model not loaded")

        seq = np.array(sequence).reshape(1, -1, 1)
        return float(self.lstm_model.predict(seq)[0][0])

    # ────────────────────────────────────────────────
    # ARIMA PREDICTION
    # ────────────────────────────────────────────────
    def predict_arima(self, steps=1):
        if self.arima_model is None:
            raise RuntimeError("ARIMA model not loaded")

        return float(self.arima_model.forecast(steps=steps)[0])

    # ────────────────────────────────────────────────
    # SARIMA PREDICTION
    # ────────────────────────────────────────────────
    def predict_sarima(self, steps=1):
        if self.sarima_model is None:
            raise RuntimeError("SARIMA model not loaded")

        return float(self.sarima_model.forecast(steps)[0])

    # ────────────────────────────────────────────────
    # LIGHTGBM PREDICTION
    # ────────────────────────────────────────────────
    def predict_lightgbm(self, features):
        if self.lightgbm_model is None:
            raise RuntimeError("LightGBM model not loaded")

        arr = np.array(features).reshape(1, -1)
        if self.scaler:
            arr = self.scaler.transform(arr)

        return float(self.lightgbm_model.predict(arr)[0])

    # ────────────────────────────────────────────────
    # CHECK WHICH MODELS ARE AVAILABLE
    # ────────────────────────────────────────────────
    def available_models(self):
        return {
            "lstm": self.lstm_model is not None,
            "arima": self.arima_model is not None,
            "sarima": self.sarima_model is not None,
            "lightgbm": self.lightgbm_model is not None,
            "scaler": self.scaler is not None
        }
