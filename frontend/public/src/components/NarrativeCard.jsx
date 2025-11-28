import { Card, CardHeader, CardTitle, CardContent } from "@/components/ui/card";
import { useState } from "react";
import { Loader2 } from "lucide-react";

export default function NarrativeCard({ onGenerate }) {
  const [inputText, setInputText] = useState("");
  const [loading, setLoading] = useState(false);
  const [narrative, setNarrative] = useState(null);

  const generateNarrative = async () => {
    if (!inputText.trim()) return;
    setLoading(true);

    try {
      const result = await onGenerate(inputText);
      setNarrative(result);
    } catch (error) {
      console.error("Narrative generation failed", error);
    }

    setLoading(false);
  };

  return (
    <Card className="w-full max-w-2xl mx-auto p-4 shadow-xl">
      <CardHeader>
        <CardTitle className="text-xl font-semibold">Narrative Prediction Engine</CardTitle>
      </CardHeader>

      <CardContent className="space-y-4">
        <textarea
          className="w-full p-3 rounded-xl border focus:outline-none focus:ring focus:ring-blue-300"
          rows="4"
          placeholder="Enter stock movement, event, or market signal to generate narrative..."
          value={inputText}
          onChange={(e) => setInputText(e.target.value)}
        />

        <button
          onClick={generateNarrative}
          className="px-4 py-2 bg-blue-600 text-white rounded-xl shadow hover:bg-blue-700 transition duration-200 flex items-center justify-center gap-2"
          disabled={loading}
        >
          {loading && <Loader2 className="animate-spin w-4 h-4" />} Generate Narrative
        </button>

        {narrative && (
          <div className="mt-4 p-4 rounded-xl bg-gray-100 border">
            <h3 className="font-semibold mb-2">Generated Narrative:</h3>
            <p className="text-gray-800 leading-relaxed whitespace-pre-wrap">{narrative}</p>
          </div>
        )}
      </CardContent>
    </Card>
  );
}