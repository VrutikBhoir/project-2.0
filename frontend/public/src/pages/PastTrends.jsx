import React, { useEffect, useState } from "react";
import ChartComponent from "../components/ChartComponent";
import api from "../services/api";
import { Loader2 } from "lucide-react";

export default function PastTrends() {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchPastTrends = async () => {
      try {
        const res = await api.get("/predict/past-trends");
        setData(res.data);
      } catch (err) {
        console.error("Failed to fetch past trends", err);
      } finally {
        setLoading(false);
      }
    };

    fetchPastTrends();
  }, []);

  if (loading) {
    return (
      <div className="flex justify-center items-center h-screen">
        <Loader2 className="w-10 h-10 animate-spin" />
      </div>
    );
  }

  if (!data) {
    return <p className="text-center mt-20 text-gray-500">No past trends data available.</p>;
  }

  return (
    <div className="max-w-6xl mx-auto px-4 py-10">
      <h1 className="text-3xl font-bold text-blue-600 mb-6">Past Trends Analysis</h1>

      {Object.keys(data).map((modelName) => (
        <ChartComponent
          key={modelName}
          title={`${modelName} Predictions`}
          labels={data[modelName].dates}
          values={data[modelName].values}
          color="#3b82f6"
        />
      ))}
    </div>
  );
}