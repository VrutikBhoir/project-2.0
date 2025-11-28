import React, { useState } from "react";
import ChartComponent from "../components/ChartComponent";
import { Loader2 } from "lucide-react";
import api from "../services/api";

export default function Predict() {
  const [symbol, setSymbol] = useState("");
  const [results, setResults] = useState(null);
  const [loading, setLoading] = useState(false);

  const handlePredict = async () => {
    if (!symbol.trim()) return;
    setLoading(true);

    try {
      const res = await api.post("/predict", { symbol });
      setResults(res.data);
    } catch (err) {
      console.error("Prediction error", err);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-screen bg-gray-50 p-6">
      <h1 className="text-4xl font-bold text-center text-blue-600 mb-6">Stock Prediction</h1>
      <p className="text-center text-gray-600 mb-10 max-w-2xl mx-auto">
        Get AI-powered predictions for your favorite stock using multiple models.
      </p>

      <div className="max-w-xl mx-auto space-y-4 mb-10">
        <input
          type="text"
          placeholder="Enter Stock Symbol (e.g., AAPL)"
          value={symbol}
          onChange={(e) => setSymbol(e.target.value)}
          className="w-full p-3 border rounded-xl focus:ring focus:ring-blue-300"
        />
        <button
          onClick={handlePredict}
          className="w-full py-3 bg-blue-600 text-white rounded-xl flex items-center justify-center gap-2 hover:bg-blue-700 transition"
          disabled={loading}
        >
          {loading && <Loader2 className="w-5 h-5 animate-spin" />} Predict
        </button>
      </div>

      {results && (
        <div className="space-y-8 max-w-4xl mx-auto">
          {Object.keys(results).map((model) => (
            <ChartComponent
              key={model}
              title={`${model} Predictions`}
              labels={results[model].dates}
              values={results[model].values}
              color="#3b82f6"
            />
          ))}
        </div>
      )}
    </div>
  );
}