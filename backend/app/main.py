from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routers import predict, realtime, risk, event, narrative, tracker
from .config import Settings
from .utils.logger import log_info

# Load global settings
settings = get_Settings()

def create_app() -> FastAPI:
    app = FastAPI(
        title="Stock Price Prediction API",
        description="Backend API for LSTM/ARIMA/SARIMA/LightGBM predictions, "
                    "Risk Engine, Event Impact, Narrative Generator, and Tracker.",
        version="1.0.0"
    )

    # Enable CORS (Frontend: React + Vite)
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],  # <-- You can restrict this in production
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # Register Routers
    app.include_router(predict.router, prefix="/api/predict", tags=["Prediction Models"])
    app.include_router(realtime.router, prefix="/api/realtime", tags=["Real-Time Data"])
    app.include_router(risk.router, prefix="/api/risk", tags=["Risk Predictor"])
    app.include_router(event.router, prefix="/api/event", tags=["Event Impact Predictor"])
    app.include_router(narrative.router, prefix="/api/narrative", tags=["Narrative Engine"])
    app.include_router(tracker.router, prefix="/api/tracker", tags=["Prediction Tracker"])

    # Health Check
    @app.get("/", tags=["Health"])
    async def root():
        return {
            "message": "Stock Price Prediction API Running Successfully",
            "status": "OK",
            "version": "1.0.0"
        }

    # Startup Event
    @app.on_event("startup")
    async def startup_event():
        log_info("🚀 API Server Started Successfully")

    return app


app = create_app()
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)