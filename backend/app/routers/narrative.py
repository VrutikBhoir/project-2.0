"""
narrative.py
-----------
Generates narrative summaries, storyline extraction, and market narratives
from raw event/news/risk signals.
"""

import logging
from typing import List, Dict, Optional
from dataclasses import dataclass

# If you use any LLM API (OpenAI, HuggingFace, Local LLM, etc.)
# You can plug in your client here
# from llm_client import LLMClient


@dataclass
class NarrativeConfig:
    model_name: str = "gpt-4o-mini"
    max_tokens: int = 300
    temperature: float = 0.4


class NarrativeGenerator:
    def __init__(self, config: NarrativeConfig):
        self.config = config
        # self.client = LLMClient(model=config.model_name)
        logging.info("Narrative Generator initialized using %s", config.model_name)

    def generate_narrative(
        self,
        events: List[Dict],
        risk_scores: Optional[Dict] = None,
        market_context: Optional[str] = None
    ) -> str:
        """
        Creates a narrative (story-style) summary of the current market, event impact,
        and risk indicators.

        Parameters:
            events: list of event dictionaries
            risk_scores: optional dict of computed risk signals
            market_context: optional string describing macro/sector trends

        Returns:
            A narrative summary string.
        """
        
        event_text = "\n".join(
            f"- {e.get('title', 'Event')}: {e.get('description', '')}"
            for e in events
        )

        risk_text = (
            "\n".join(f"{k}: {v}" for k, v in risk_scores.items())
            if risk_scores else "No risk indicators available."
        )

        prompt = f"""
You are a financial narrative generator. Combine the following into a clear,
concise narrative explaining the market situation:

Events:
{event_text}

Risk Indicators:
{risk_text}

Market Context:
{market_context or "Not provided"}

Generate a 4–6 sentence narrative capturing the storyline, causes, and likely outcomes.
Avoid fluff. Keep it realistic and analytical.
"""

        # response = self.client.generate(prompt, max_tokens=self.config.max_tokens)

        # For now, returning a mock output (remove once LLM is integrated)
        return (
            "Market narrative generation placeholder. "
            "Integrate LLM API to produce narratives."
        )

    def summarize_event(self, event: Dict) -> str:
        """
        Short 1-2 sentence AI summary for a single event.
        """
        title = event.get("title", "Event")
        desc = event.get("description", "")

        prompt = f"Summarize the following in 2 sentences:\nTitle: {title}\nDetails: {desc}"

        # response = self.client.generate(prompt)
        return "Event summary placeholder."

    def batch_summarize(self, events: List[Dict]) -> List[str]:
        """
        Summarize multiple events.
        """
        return [self.summarize_event(e) for e in events]
