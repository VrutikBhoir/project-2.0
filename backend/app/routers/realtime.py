"""
realtime.py
-----------
Real-time orchestrator for:
- Market data ingestion
- Event detection (event.py)
- Risk scoring (risk_model.py)
- Narrative generation (narrative.py)

Integrates all models to provide live insights.
"""

import time
import logging
from typing import Dict, Any

from event import EventDetector
from risk_model import RiskModel
from narrative import NarrativeGenerator, NarrativeConfig


class RealTimePipeline:
    def __init__(
        self,
        event_model_path: str,
        risk_model_path: str,
        poll_interval: int = 10
    ):
        """
        Initializes the real-time engine.
        
        Parameters:
            event_model_path: path to trained event classification model
            risk_model_path: path to trained risk model
            poll_interval: seconds between each polling of live data
        """

        self.event_detector = EventDetector(model_path=event_model_path)
        self.risk_model = RiskModel(model_path=risk_model_path)
        self.narrative_gen = NarrativeGenerator(NarrativeConfig())
        self.poll_interval = poll_interval
        
        logging.info("Real-time pipeline initialized.")
    
    def fetch_live_data(self) -> Dict[str, Any]:
        """
        Fetch real-time data from APIs (market, news, sentiment).
        
        Replace this with actual API integrations.
        """
        return {
            "timestamp": time.time(),
            "news": "Fed signals rate cut possibility; markets react positively.",
            "market_data": {
                "nifty": 0.45,
                "banknifty": -0.12,
                "crude_oil": 1.8
            }
        }

    def process(self):
        """
        Runs one full real-time cycle:
        1. Ingest data
        2. Detect events
        3. Compute risk
        4. Generate narrative
        """

        # Step 1: Load data
        data = self.fetch_live_data()
        logging.info("Fetched live data.")

        # Step 2: Event Detection
        events = self.event_detector.detect(data["news"])
        logging.info("Event detection complete: %s", events)

        # Step 3: Risk Scoring
        risk_scores = self.risk_model.predict(data["market_data"])
        logging.info("Risk model scored: %s", risk_scores)

        # Step 4: Narrative
        narrative = self.narrative_gen.generate_narrative(
            events=events,
            risk_scores=risk_scores,
            market_context="Intraday market behavior based on latest data."
        )

        logging.info("Narrative generated.")
        
        return {
            "events": events,
            "risk": risk_scores,
            "narrative": narrative,
            "timestamp": data["timestamp"]
        }

    def start(self):
        """
        Continuous loop for real-time operation.
        """
        logging.info("Real-time pipeline started.")
        while True:
            output = self.process()
            print("\n=== REALTIME OUTPUT ===")
            print("Events:", output["events"])
            print("Risk:", output["risk"])
            print("Narrative:", output["narrative"])
            print("========================\n")
            time.sleep(self.poll_interval)
