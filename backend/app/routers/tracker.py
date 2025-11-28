from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from app.dependencies import get_app_settings
from app.services.tracker_engine import TrackerEngine
from app.config import Settings

router = APIRouter()


# ───────────────────────────────
# REQUEST SCHEMAS
# ───────────────────────────────
class PredictionLog(BaseModel):
    ticker: str
    timestamp: str
    predicted_price: float
    model_used: str


class RealityLog(BaseModel):
    ticker: str
    timestamp: str
    actual_price: float


# ───────────────────────────────
# POST /api/tracker/log_prediction
# ───────────────────────────────
@router.post("/log_prediction")
async def log_prediction(
    data: PredictionLog,
    settings: Settings = Depends(get_app_settings)
):
    try:
        tracker = TrackerEngine(settings)
        tracker.log_prediction(
            ticker=data.ticker,
            timestamp=data.timestamp,
            model=data.model_used,
            predicted=data.predicted_price
        )
        return {"message": "Prediction logged successfully"}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# ───────────────────────────────
# POST /api/tracker/log_reality
# ───────────────────────────────
@router.post("/log_reality")
async def log_reality(
    data: RealityLog,
    settings: Settings = Depends(get_app_settings)
):
    try:
        tracker = TrackerEngine(settings)
        tracker.log_actual(
            ticker=data.ticker,
            timestamp=data.timestamp,
            actual=data.actual_price
        )
        return {"message": "Actual market data logged successfully"}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# ───────────────────────────────
# GET /api/tracker/compare?ticker=AAPL
# ───────────────────────────────
@router.get("/compare")
async def compare_predictions(
    ticker: str,
    settings: Settings = Depends(get_app_settings)
):
    try:
        tracker = TrackerEngine(settings)
        result = tracker.compare(ticker)

        return {
            "ticker": ticker,
            "data_points": result["count"],
            "average_error": result["avg_error"],
            "mape": result["mape"],
            "highest_error": result["max_error"],
            "predictions": result["merged_data"]
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# ───────────────────────────────
# GET /api/tracker/accuracy?ticker=AAPL
# ───────────────────────────────
@router.get("/accuracy")
async def get_accuracy(
    ticker: str,
    settings: Settings = Depends(get_app_settings)
):
    try:
        tracker = TrackerEngine(settings)
        accuracy = tracker.compute_accuracy(ticker)

        return {
            "ticker": ticker,
            "accuracy_percent": accuracy,
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# ───────────────────────────────
# GET /api/tracker/stats
# ───────────────────────────────
@router.get("/stats")
async def tracker_statistics(
    settings: Settings = Depends(get_app_settings)
):
    try:
        tracker = TrackerEngine(settings)
        stats = tracker.global_stats()

        return stats

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
