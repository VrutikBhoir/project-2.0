import os
import json
import time
import logging
import requests
from typing import Dict, Optional
from app.config import Settings


class RealtimeSource:
    """
    Handles fetching, caching, and providing real-time data.
    Supports API or simulated data.
    """

    def __init__(self, settings: Settings):
        self.settings = settings
        self.cache_file = os.path.join(settings.BASE_DIR, "data", "realtime_cache.json")
        self.cache_ttl = 60  # seconds

        # Ensure cache file exists
        if not os.path.exists(self.cache_file):
            with open(self.cache_file, "w") as f:
                json.dump({}, f)

        logging.info("RealtimeSource initialized.")

    # ────────────────────────────────────────────────
    # FETCH DATA FROM API
    # ────────────────────────────────────────────────
    def fetch_from_api(self, symbol: str) -> Dict:
        """
        Fetch real-time market data from external API.
        You can replace this with any provider (Yahoo, AlphaVantage, Finnhub, etc.)
        """
        try:
            api_key = self.settings.REALTIME_API_KEY
            url = f"https://finnhub.io/api/v1/quote?symbol={symbol}&token={api_key}"
            response = requests.get(url, timeout=5)
            response.raise_for_status()
            data = response.json()

            return {
                "current_price": data.get("c"),
                "high": data.get("h"),
                "low": data.get("l"),
                "open": data.get("o"),
                "previous_close": data.get("pc"),
                "timestamp": int(time.time())
            }

        except Exception as e:
            logging.warning(f"Failed to fetch real-time data for {symbol}: {e}")
            return self.fetch_from_cache(symbol)

    # ────────────────────────────────────────────────
    # READ CACHE
    # ────────────────────────────────────────────────
    def fetch_from_cache(self, symbol: str) -> Dict:
        """
        Fetch cached data if available
        """
        with open(self.cache_file, "r") as f:
            cache = json.load(f)

        if symbol in cache:
            cached_entry = cache[symbol]
            # Check TTL
            if time.time() - cached_entry.get("timestamp", 0) < self.cache_ttl:
                return cached_entry
            else:
                logging.info(f"Cache expired for {symbol}")
        return {"message": f"No recent data for {symbol}"}

    # ────────────────────────────────────────────────
    # UPDATE CACHE
    # ────────────────────────────────────────────────
    def update_cache(self, symbol: str, data: Dict):
        """
        Save latest data to cache
        """
        with open(self.cache_file, "r") as f:
            cache = json.load(f)

        cache[symbol] = data

        with open(self.cache_file, "w") as f:
            json.dump(cache, f, indent=2)

    # ────────────────────────────────────────────────
    # GET REAL-TIME DATA (FETCH + CACHE)
    # ────────────────────────────────────────────────
    def get_data(self, symbol: str) -> Dict:
        """
        Main method called by router:
        - Fetch from API
        - Update cache
        - Return latest data
        """
        data = self.fetch_from_api(symbol)
        if "current_price" in data:
            self.update_cache(symbol, data)
        return data
