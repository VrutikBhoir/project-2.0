import React, { useEffect, useState } from "react";
import ChartComponent from "../components/ChartComponent";
import { Loader2 } from "lucide-react";

export default function Realtime() {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchRealtime = async () => {
      try {
        const res = await fetch("http://localhost:8000/realtime/get");
        const result = await res.json();
        setData(result);
      } catch (err) {
        console.error("Realtime fetch error", err);
      } finally {
        setLoading(false);
      }
    };

    fetchRealtime();
    const interval = setInterval(fetchRealtime, 10000); // Refresh every 10s
    return () => clearInterval(interval);
  }, []);

  if (loading) {
    return (
      <div className="flex justify-center items-center h-screen">
        <Loader2 className="w-10 h-10 animate-spin" />
      </div>
    );
  }

  if (!data) {
    return <p className="text-center mt-20 text-gray-500">No real-time data available.</p>;
  }

  return (
    <div className="max-w-6xl mx-auto px-4 py-10">
      <h1 className="text-3xl font-bold text-blue-600 mb-6">Real-Time Stock Data</h1>
      {Object.keys(data).map((symbol) => (
        <ChartComponent
          key={symbol}
          title={`${symbol} Real-Time`}
          labels={data[symbol].timestamps}
          values={data[symbol].prices}
          color="#10b981"
        />
      ))}
    </div>
  );
}