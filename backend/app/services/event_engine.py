import numpy as np
from app.config import Settings
from sklearn.preprocessing import MinMaxScaler
import joblib
import json
import os


class EventEngine:
    def __init__(self, settings: Settings):
        self.settings = settings

        # Path to model directory
        self.model_dir = os.path.join(settings.BASE_DIR, "app", "models")

        # Try loading the model (fallback = rule-based)
        self.model = None
        self.scaler = None

        self._load_model()

    # ────────────────────────────────────────────────
    # LOAD MODEL + SCALER
    # ────────────────────────────────────────────────
    def _load_model(self):
        try:
            model_path = os.path.join(self.model_dir, "event_impact_model.pkl")
            scaler_path = os.path.join(self.model_dir, "scaler.pkl")

            if os.path.exists(model_path):
                self.model = joblib.load(model_path)

            if os.path.exists(scaler_path):
                self.scaler = joblib.load(scaler_path)

        except Exception:
            self.model = None


    # ────────────────────────────────────────────────
    # MAIN EVENT IMPACT PREDICTOR
    # ────────────────────────────────────────────────
    def predict_event_impact(self, event: str, sentiment: float, volatility: float):
        """
        Predicts market movement impact based on:
        - event description (text embedding = simplified)
        - sentiment score
        - volatility
        """

        # STEP 1 → Convert event text to simple numerical features (placeholder)
        event_features = self._text_to_features(event)

        # STEP 2 → Build feature array
        features = np.array([
            event_features["keyword_strength"],
            sentiment,
            volatility
        ]).reshape(1, -1)

        # STEP 3 → If ML model exists, use it
        if self.model is not None and self.scaler is not None:
            scaled = self.scaler.transform(features)
            prediction = self.model.predict(scaled)[0]
            confidence = min(0.95, 0.55 + (abs(prediction) * 0.3))

            return self._format_output(
                event=event,
                sentiment=sentiment,
                volatility=volatility,
                impact_score=float(prediction),
                confidence=round(float(confidence), 3)
            )

        # STEP 4 → Fallback → Rule-based engine
        return self._rule_based_prediction(event, sentiment, volatility)


    # ────────────────────────────────────────────────
    # TEXT → NUMERICAL FEATURE EXTRACTION
    # ────────────────────────────────────────────────
    def _text_to_features(self, text: str):
        text_lower = text.lower()

        KEYWORDS = {
            "earnings": 0.8,
            "inflation": 0.7,
            "rate hike": 0.9,
            "war": 1.0,
            "merger": 0.6,
            "acquisition": 0.6,
            "bankruptcy": 1.0,
            "lawsuit": 0.7,
            "regulation": 0.5,
        }

        strength = 0.3  # Default baseline

        for word, value in KEYWORDS.items():
            if word in text_lower:
                strength = max(strength, value)

        return {"keyword_strength": strength}


    # ────────────────────────────────────────────────
    # RULE-BASED IMPACT ENGINE (if model not found)
    # ────────────────────────────────────────────────
    def _rule_based_prediction(self, event, sentiment, volatility):
        """ Generates a fallback prediction """

        # Basic formula
        impact = (
            (sentiment * 0.4) -
            (volatility * 0.3) +
            (self._text_to_features(event)["keyword_strength"] * 0.8)
        )

        # Normalize to -1 to +1
        impact = max(-1, min(1, impact))

        confidence = 0.55 + (abs(impact) * 0.3)

        return self._format_output(
            event=event,
            sentiment=sentiment,
            volatility=volatility,
            impact_score=round(float(impact), 4),
            confidence=round(float(confidence), 3)
        )


    # ────────────────────────────────────────────────
    # FORMAT OUTPUT FOR API RESPONSE
    # ────────────────────────────────────────────────
    def _format_output(self, event, sentiment, volatility, impact_score, confidence):
        if impact_score > 0.4:
            impact_label = "Strong Positive"
        elif impact_score > 0.1:
            impact_label = "Mild Positive"
        elif impact_score < -0.4:
            impact_label = "Strong Negative"
        elif impact_score < -0.1:
            impact_label = "Mild Negative"
        else:
            impact_label = "Neutral"

        return {
            "event": event,
            "impact_label": impact_label,
            "impact_score": impact_score,
            "confidence": confidence,
            "inputs_used": {
                "sentiment": sentiment,
                "volatility": volatility
            },
            "explanation": f"The event '{event}' combined with sentiment and volatility suggests a {impact_label} impact."
        }
