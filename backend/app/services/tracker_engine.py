import os
import json
import logging
from typing import Dict, List, Optional
from app.config import Settings


class TrackerEngine:
    """
    Prediction vs Reality Tracker Engine
    Stores predictions and actuals, calculates accuracy metrics.
    """

    def __init__(self, settings: Settings):
        self.settings = settings
        self.storage_file = os.path.join(settings.BASE_DIR, "data", "prediction_tracker.json")

        # Initialize storage file if it does not exist
        if not os.path.exists(self.storage_file):
            with open(self.storage_file, "w") as f:
                json.dump([], f, indent=2)

        logging.info("TrackerEngine initialized.")

    # ────────────────────────────────────────────────
    # LOG A NEW PREDICTION AND ACTUAL VALUE
    # ────────────────────────────────────────────────
    def log_prediction(
        self,
        model_name: str,
        symbol: str,
        predicted_value: float,
        actual_value: Optional[float] = None,
        timestamp: Optional[int] = None
    ) -> Dict:
        """
        Logs prediction and optionally actual value.
        """
        entry = {
            "model_name": model_name,
            "symbol": symbol,
            "predicted_value": predicted_value,
            "actual_value": actual_value,
            "timestamp": timestamp or int(__import__("time").time())
        }

        data = self._read_storage()
        data.append(entry)
        self._write_storage(data)

        return entry

    # ────────────────────────────────────────────────
    # GET ALL TRACKED PREDICTIONS
    # ────────────────────────────────────────────────
    def get_all(self) -> List[Dict]:
        return self._read_storage()

    # ────────────────────────────────────────────────
    # CALCULATE ACCURACY METRICS
    # ────────────────────────────────────────────────
    def calculate_accuracy(self, model_name: Optional[str] = None) -> Dict:
        """
        Returns RMSE and MAE for tracked predictions
        """
        import math

        data = self._read_storage()
        if model_name:
            data = [d for d in data if d["model_name"] == model_name]

        actuals = [d["actual_value"] for d in data if d["actual_value"] is not None]
        preds = [d["predicted_value"] for d in data if d["actual_value"] is not None]

        if not actuals or not preds:
            return {"rmse": None, "mae": None, "count": 0}

        mse = sum((a - p) ** 2 for a, p in zip(actuals, preds)) / len(actuals)
        mae = sum(abs(a - p) for a, p in zip(actuals, preds)) / len(actuals)
        rmse = math.sqrt(mse)

        return {"rmse": round(rmse, 4), "mae": round(mae, 4), "count": len(actuals)}

    # ────────────────────────────────────────────────
    # INTERNAL: READ STORAGE
    # ────────────────────────────────────────────────
    def _read_storage(self) -> List[Dict]:
        try:
            with open(self.storage_file, "r") as f:
                return json.load(f)
        except Exception as e:
            logging.warning(f"Failed to read tracker storage: {e}")
            return []

    # ────────────────────────────────────────────────
    # INTERNAL: WRITE STORAGE
    # ────────────────────────────────────────────────
    def _write_storage(self, data: List[Dict]):
        try:
            with open(self.storage_file, "w") as f:
                json.dump(data, f, indent=2)
        except Exception as e:
            logging.warning(f"Failed to write tracker storage: {e}")
