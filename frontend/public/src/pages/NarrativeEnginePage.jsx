import React, { useState } from "react";
import NarrativeCard from "../components/NarrativeCard";
import { Loader2 } from "lucide-react";

export default function NarrativeEnginePage() {
  const [input, setInput] = useState("");
  const [narrative, setNarrative] = useState(null);
  const [loading, setLoading] = useState(false);

  const generateNarrative = async () => {
    if (!input.trim()) return;
    setLoading(true);

    try {
      const res = await fetch("http://localhost:8000/narrative/predict", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ symbol: input }),
      });
      const data = await res.json();
      setNarrative(data.narrative);
    } catch (err) {
      console.error("Narrative generation error", err);
      setNarrative("Failed to generate narrative.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-screen bg-gray-50 p-6">
      <h1 className="text-4xl font-bold text-center text-blue-600 mb-6">
        AI Narrative Engine
      </h1>

      <p className="text-center text-gray-600 mb-10 max-w-2xl mx-auto">
        Generate AI-driven narrative explanations for stock price trends.
      </p>

      <div className="max-w-xl mx-auto space-y-4">
        <input
          type="text"
          placeholder="Enter Stock Symbol (e.g., AAPL)"
          value={input}
          onChange={(e) => setInput(e.target.value)}
          className="w-full p-3 border rounded-xl focus:ring focus:ring-blue-300"
        />

        <button
          onClick={generateNarrative}
          className="w-full py-3 bg-blue-600 text-white rounded-xl flex items-center justify-center gap-2 hover:bg-blue-700 transition"
          disabled={loading}
        >
          {loading && <Loader2 className="w-5 h-5 animate-spin" />} Generate Narrative
        </button>
      </div>

      {narrative && (
        <div className="mt-10">
          <NarrativeCard narrative={narrative} />
        </div>
      )}
    </div>
  );
}