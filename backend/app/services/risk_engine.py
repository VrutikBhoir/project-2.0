import os
import numpy as np
import joblib
from app.config import Settings
import logging


class RiskEngine:
    """
    AI Risk Predictor Engine
    Calculates risk score for stocks/events based on features and optional ML model.
    """

    def __init__(self, settings: Settings):
        self.settings = settings
        self.model_dir = os.path.join(settings.BASE_DIR, "app", "models")
        self.model = None
        self.scaler = None
        self._load_model()
        logging.info("RiskEngine initialized.")

    # ────────────────────────────────────────────────
    # LOAD ML MODEL IF AVAILABLE
    # ────────────────────────────────────────────────
    def _load_model(self):
        try:
            model_path = os.path.join(self.model_dir, "risk_model.pkl")
            scaler_path = os.path.join(self.model_dir, "scaler.pkl")

            if os.path.exists(model_path):
                self.model = joblib.load(model_path)

            if os.path.exists(scaler_path):
                self.scaler = joblib.load(scaler_path)

        except Exception as e:
            logging.warning(f"Could not load risk model: {e}")
            self.model = None
            self.scaler = None

    # ────────────────────────────────────────────────
    # PREDICT RISK SCORE
    # ────────────────────────────────────────────────
    def predict(
        self,
        volatility: float,
        sentiment: float,
        liquidity: float,
        event_severity: float = 0.0
    ) -> dict:
        """
        Returns risk score and risk category
        """

        features = np.array([volatility, sentiment, liquidity, event_severity]).reshape(1, -1)

        if self.model and self.scaler:
            scaled_features = self.scaler.transform(features)
            score = float(self.model.predict(scaled_features)[0])
        else:
            # Fallback rule-based calculation
            score = 0.4 * volatility - 0.3 * sentiment + 0.2 * liquidity + 0.1 * event_severity
            score = max(0, min(1, score))  # normalize to [0,1]

        category = self._risk_category(score)

        return {
            "risk_score": round(score, 3),
            "risk_category": category,
            "inputs_used": {
                "volatility": volatility,
                "sentiment": sentiment,
                "liquidity": liquidity,
                "event_severity": event_severity
            },
            "explanation": f"The calculated risk is {category} based on the given inputs."
        }

    # ────────────────────────────────────────────────
    # RISK CATEGORY
    # ────────────────────────────────────────────────
    def _risk_category(self, score: float) -> str:
        if score >= 0.7:
            return "High Risk"
        elif score >= 0.4:
            return "Medium Risk"
        else:
            return "Low Risk"
