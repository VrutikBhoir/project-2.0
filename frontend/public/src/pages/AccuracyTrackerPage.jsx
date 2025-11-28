import React, { useEffect, useState } from "react";
import PredictionTracker from "../components/PredictionTracker";
import api from "../services/api";

export default function AccuracyTrackerPage() {
  const [trackerData, setTrackerData] = useState([]);

  const fetchTracker = async () => {
    try {
      const res = await api.get("/tracker/get");
      return res.data;
    } catch (err) {
      console.error("Error fetching tracker data", err);
      return [];
    }
  };

  useEffect(() => {
    const load = async () => {
      const data = await fetchTracker();
      setTrackerData(data);
    };
    load();
  }, []);

  return (
    <div className="max-w-6xl mx-auto px-4 py-10">
      <h1 className="text-3xl font-bold text-blue-600 mb-6">
        Prediction vs Reality Tracker
      </h1>

      <PredictionTracker fetchTracker={fetchTracker} />
    </div>
  );
}