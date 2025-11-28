import { Card, CardHeader, CardTitle, CardContent } from "@/components/ui/card";
import { useEffect, useState } from "react";
import { Loader2 } from "lucide-react";

export default function PredictionTracker({ fetchTracker }) {
  const [data, setData] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const loadData = async () => {
      try {
        const result = await fetchTracker();
        setData(result || []);
      } catch (error) {
        console.error("Tracker fetch error", error);
      }
      setLoading(false);
    };

    loadData();
  }, [fetchTracker]);

  return (
    <Card className="w-full max-w-4xl mx-auto p-4 shadow-xl">
      <CardHeader>
        <CardTitle className="text-xl font-semibold">Prediction vs Reality Tracker</CardTitle>
      </CardHeader>

      <CardContent>
        {loading ? (
          <div className="flex items-center justify-center py-6">
            <Loader2 className="animate-spin w-6 h-6 text-blue-600" />
          </div>
        ) : (
          <div className="overflow-x-auto">
            <table className="w-full border-collapse">
              <thead>
                <tr className="bg-gray-200 text-left">
                  <th className="p-3">Date</th>
                  <th className="p-3">Predicted Price</th>
                  <th className="p-3">Actual Price</th>
                  <th className="p-3">Error (%)</th>
                </tr>
              </thead>
              <tbody>
                {data.length === 0 && (
                  <tr>
                    <td colSpan="4" className="text-center p-4 text-gray-500">
                      No tracking data available.
                    </td>
                  </tr>
                )}

                {data.map((row, idx) => (
                  <tr key={idx} className="border-b hover:bg-gray-50">
                    <td className="p-3">{row.date}</td>
                    <td className="p-3">₹{row.predicted}</td>
                    <td className="p-3">₹{row.actual}</td>
                    <td className="p-3 text-blue-600 font-semibold">{row.error}%</td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        )}
      </CardContent>
    </Card>
  );
}