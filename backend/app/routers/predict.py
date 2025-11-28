from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from typing import List
from app.dependencies import get_model_handler
from app.services.model_handler import ModelHandler


router = APIRouter()


# ─────────────────────────────────────────────
# REQUEST MODEL
# ─────────────────────────────────────────────
class PredictInput(BaseModel):
    data: List[float]      # last N closing prices
    steps: int = 1         # number of future predictions


# ─────────────────────────────────────────────
# PREDICT USING LSTM
# ─────────────────────────────────────────────
@router.post("/lstm")
async def predict_lstm(
    request: PredictInput,
    model: ModelHandler = Depends(get_model_handler)
):
    try:
        output = model.predict_lstm(request.data, request.steps)
        return {"model": "LSTM", "prediction": output}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# ─────────────────────────────────────────────
# PREDICT USING ARIMA
# ─────────────────────────────────────────────
@router.post("/arima")
async def predict_arima(
    request: PredictInput,
    model: ModelHandler = Depends(get_model_handler)
):
    try:
        output = model.predict_arima(request.data, request.steps)
        return {"model": "ARIMA", "prediction": output}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# ─────────────────────────────────────────────
# PREDICT USING SARIMA
# ─────────────────────────────────────────────
@router.post("/sarima")
async def predict_sarima(
    request: PredictInput,
    model: ModelHandler = Depends(get_model_handler)
):
    try:
        output = model.predict_sarima(request.data, request.steps)
        return {"model": "SARIMA", "prediction": output}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# ─────────────────────────────────────────────
# PREDICT USING LIGHTGBM
# ─────────────────────────────────────────────
@router.post("/lightgbm")
async def predict_lightgbm(
    request: PredictInput,
    model: ModelHandler = Depends(get_model_handler)
):
    try:
        output = model.predict_lightgbm(request.data, request.steps)
        return {"model": "LightGBM", "prediction": output}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# ─────────────────────────────────────────────
# MULTI-MODEL COMPARE ENDPOINT
# ─────────────────────────────────────────────
@router.post("/compare")
async def compare_models(
    request: PredictInput,
    model: ModelHandler = Depends(get_model_handler)
):
    try:
        return {
            "LSTM": model.predict_lstm(request.data, request.steps),
            "ARIMA": model.predict_arima(request.data, request.steps),
            "SARIMA": model.predict_sarima(request.data, request.steps),
            "LightGBM": model.predict_lightgbm(request.data, request.steps),
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
