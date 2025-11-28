import React, { useState } from "react";
import api from "../services/api";
import { Card, CardHeader, CardTitle, CardContent } from "@/components/ui/card";
import { Loader2 } from "lucide-react";
import ChartComponent from "../components/ChartComponent";

export default function CompareModels() {
  const [symbol, setSymbol] = useState("");
  const [loading, setLoading] = useState(false);
  const [results, setResults] = useState(null);

  const compare = async () => {
    if (!symbol.trim()) return;
    setLoading(true);

    try {
      const res = await api.post("/predict/compare", { symbol });
      setResults(res.data);
    } catch (error) {
      console.error("Model comparison error", error);
    }

    setLoading(false);
  };

  return (
    <div className="max-w-6xl mx-auto px-4 py-10">
      <h1 className="text-3xl font-bold text-blue-600 mb-6">Compare Models</h1>

      <Card className="p-6 shadow-xl">
        <CardHeader>
          <CardTitle>Enter Stock Symbol</CardTitle>
        </CardHeader>

        <CardContent className="space-y-4">
          <input
            type="text"
            placeholder="e.g., AAPL, TSLA"
            value={symbol}
            onChange={(e) => setSymbol(e.target.value)}
            className="w-full p-3 border rounded-xl focus:ring focus:ring-blue-300"
          />

          <button
            onClick={compare}
            className="px-4 py-2 bg-blue-600 text-white rounded-xl hover:bg-blue-700 transition flex items-center justify-center gap-2"
            disabled={loading}
          >
            {loading && <Loader2 className="animate-spin w-4 h-4" />} Compare Models
          </button>
        </CardContent>
      </Card>

      {results && (
        <div className="mt-10 space-y-8">
          {/* LSTM */}
          <ChartComponent
            title="LSTM Model Prediction"
            labels={results.dates}
            values={results.lstm}
            color="#3b82f6"
          />

          {/* ARIMA */}
          <ChartComponent
            title="ARIMA Model Prediction"
            labels={results.dates}
            values={results.arima}
            color="#10b981"
          />

          {/* SARIMA */}
          <ChartComponent
            title="SARIMA Model Prediction"
            labels={results.dates}
            values={results.sarima}
            color="#f59e0b"
          />

          {/* LightGBM */}
          <ChartComponent
            title="LightGBM Model Prediction"
            labels={results.dates}
            values={results.lightgbm}
            color="#ef4444"
          />
        </div>
      )}
    </div>
  );
}