from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from app.dependencies import get_app_settings
from app.services.risk_engine import RiskEngine
from app.config import Settings

router = APIRouter()


# ────────────────────────────────────────────
# REQUEST BODY SCHEMA
# ────────────────────────────────────────────
class RiskInput(BaseModel):
    ticker: str
    price: float
    volume: float
    volatility: float
    sentiment_score: float = 0.0    # optional
    macro_index: float = 0.0        # optional


# ────────────────────────────────────────────
# POST /api/risk/predict
# ────────────────────────────────────────────
@router.post("/predict")
async def predict_risk(
    data: RiskInput,
    settings: Settings = Depends(get_app_settings)
):
    try:
        risk_engine = RiskEngine(settings)

        result = risk_engine.predict_risk(
            ticker=data.ticker,
            price=data.price,
            volume=data.volume,
            volatility=data.volatility,
            sentiment=data.sentiment_score,
            macro_index=data.macro_index
        )

        return {
            "ticker": data.ticker,
            "risk_level": result["risk_level"],
            "risk_score": result["risk_score"],
            "confidence": result["confidence"],
            "indicators_used": result["indicators"],
            "reasoning": result["reasoning"]
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# ────────────────────────────────────────────
# SAMPLE ENDPOINT FOR TESTING
# ────────────────────────────────────────────
@router.get("/samples")
async def sample_risk_inputs():
    return {
        "example_inputs": [
            {
                "ticker": "AAPL",
                "price": 187.23,
                "volume": 32100000,
                "volatility": 0.028,
                "sentiment_score": 0.65,
                "macro_index": 0.4,
                "expected_risk": "Low"
            },
            {
                "ticker": "TSLA",
                "price": 244.89,
                "volume": 59000000,
                "volatility": 0.091,
                "sentiment_score": -0.3,
                "macro_index": -0.15,
                "expected_risk": "High"
            }
        ]
    }
