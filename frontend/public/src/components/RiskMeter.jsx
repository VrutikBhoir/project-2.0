import { useState } from "react";
import { Card, CardHeader, CardTitle, CardContent } from "@/components/ui/card";
import { Loader2 } from "lucide-react";

export default function RiskMeter({ onCalculate }) {
  const [stock, setStock] = useState("");
  const [risk, setRisk] = useState(null);
  const [loading, setLoading] = useState(false);

  const calculate = async () => {
    if (!stock.trim()) return;
    setLoading(true);

    try {
      const result = await onCalculate(stock);
      setRisk(result);
    } catch (error) {
      console.error("Risk calculation error", error);
    }

    setLoading(false);
  };

  const getRiskColor = (value) => {
    if (value < 30) return "text-green-600";
    if (value < 60) return "text-yellow-500";
    return "text-red-600";
  };

  return (
    <Card className="w-full max-w-xl mx-auto p-4 shadow-xl">
      <CardHeader>
        <CardTitle className="text-xl font-semibold">AI Risk Predictor</CardTitle>
      </CardHeader>

      <CardContent className="space-y-4">
        <input
          type="text"
          placeholder="Enter Stock Symbol (e.g., AAPL, TSLA)"
          value={stock}
          onChange={(e) => setStock(e.target.value)}
          className="w-full p-3 border rounded-xl focus:ring focus:ring-blue-300"
        />

        <button
          onClick={calculate}
          className="px-4 py-2 bg-blue-600 text-white rounded-xl hover:bg-blue-700 transition flex items-center justify-center gap-2"
          disabled={loading}
        >
          {loading && <Loader2 className="w-4 h-4 animate-spin" />} Calculate Risk
        </button>

        {risk !== null && (
          <div className="p-4 bg-gray-100 border rounded-xl mt-4">
            <h3 className="font-semibold mb-2">Risk Score</h3>
            <p className={`text-3xl font-bold ${getRiskColor(risk)}`}>{risk}%</p>

            <p className="mt-2 text-gray-700">
              {risk < 30 && "Low Risk — Stable market conditions."}
              {risk >= 30 && risk < 60 && "Moderate Risk — Watch for volatility."}
              {risk >= 60 && "High Risk — High volatility expected, be cautious."}
            </p>
          </div>
        )}
      </CardContent>
    </Card>
  );
}
