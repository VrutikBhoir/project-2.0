from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from app.dependencies import get_app_settings
from app.services.event_engine import EventImpactEngine
from app.config import Settings


router = APIRouter()


# ────────────────────────────────────────────
# REQUEST SCHEMA
# ────────────────────────────────────────────
class EventInput(BaseModel):
    headline: str         # short event headline
    description: str = "" # optional extended info
    ticker: str = ""      # optional stock symbol


# ────────────────────────────────────────────
# EVENT IMPACT PREDICTION
# ────────────────────────────────────────────
@router.post("/predict")
async def predict_event_impact(
    request: EventInput,
    settings: Settings = Depends(get_app_settings)
):
    try:
        engine = EventImpactEngine(settings)

        result = engine.predict_event_impact(
            headline=request.headline,
            description=request.description,
            ticker=request.ticker
        )

        return {
            "event_headline": request.headline,
            "ticker": request.ticker if request.ticker else "N/A",
            "impact": result["impact"],
            "confidence": result["confidence"],
            "impact_score": result["impact_score"],
            "reasoning": result["reasoning"]
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# ────────────────────────────────────────────
# SAMPLE EVENTS FOR TESTING
# ────────────────────────────────────────────
@router.get("/samples")
async def sample_events():
    return {
        "examples": [
            {
                "headline": "Federal Reserve increases interest rates by 0.25%",
                "expected_impact": "Negative"
            },
            {
                "headline": "Apple announces record quarterly profits",
                "expected_impact": "Positive"
            },
            {
                "headline": "Oil prices remain stable amid global uncertainty",
                "expected_impact": "Neutral"
            }
        ]
    }
