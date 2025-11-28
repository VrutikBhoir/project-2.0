import React, { useState } from "react";
import RiskMeter from "../components/RiskMeter";
import { Loader2 } from "lucide-react";

export default function RiskPredictionPage() {
  const [symbol, setSymbol] = useState("");
  const [riskScore, setRiskScore] = useState(null);
  const [loading, setLoading] = useState(false);

  const getRiskScore = async () => {
    if (!symbol.trim()) return;
    setLoading(true);

    try {
      const res = await fetch("http://localhost:8000/risk/predict", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ symbol }),
      });
      const data = await res.json();
      setRiskScore(data.score);
    } catch (err) {
      console.error("Risk prediction error", err);
      setRiskScore(null);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-screen bg-gray-50 p-6">
      <h1 className="text-4xl font-bold text-center text-blue-600 mb-6">
        AI Risk Predictor
      </h1>
      <p className="text-center text-gray-600 mb-10 max-w-2xl mx-auto">
        Compute a risk score for stocks using AI-powered risk prediction models.
      </p>

      <div className="max-w-xl mx-auto space-y-4">
        <input
          type="text"
          placeholder="Enter Stock Symbol (e.g., AAPL)"
          value={symbol}
          onChange={(e) => setSymbol(e.target.value)}
          className="w-full p-3 border rounded-xl focus:ring focus:ring-blue-300"
        />

        <button
          onClick={getRiskScore}
          className="w-full py-3 bg-blue-600 text-white rounded-xl flex items-center justify-center gap-2 hover:bg-blue-700 transition"
          disabled={loading}
        >
          {loading && <Loader2 className="w-5 h-5 animate-spin" />} Calculate Risk
        </button>
      </div>

      {riskScore !== null && (
        <div className="mt-10 max-w-md mx-auto">
          <RiskMeter score={riskScore} />
        </div>
      )}
    </div>
  );
}