import React, { useEffect, useState } from "react";
import EventImpactCard from "../components/EventImpactCard";
import { Loader2 } from "lucide-react";

export default function EventImpactPage() {
  const [events, setEvents] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchEvents = async () => {
      try {
        const res = await fetch("http://localhost:8000/event-impact/latest");
        const data = await res.json();
        setEvents(data.events || []);
      } catch (err) {
        console.error("Failed to fetch event impacts", err);
      } finally {
        setLoading(false);
      }
    };

    fetchEvents();
  }, []);

  return (
    <div className="min-h-screen bg-gray-50 p-6">
      <h1 className="text-4xl font-bold text-center mb-6">Event Impact Analysis</h1>
      <p className="text-center text-gray-600 mb-10 max-w-2xl mx-auto">
        Understand how global events influence stock markets with AI-powered analysis.
      </p>

      {loading ? (
        <div className="flex justify-center mt-20">
          <Loader2 className="w-10 h-10 animate-spin" />
        </div>
      ) : (
        <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-6">
          {events.length > 0 ? (
            events.map((event, index) => (
              <EventImpactCard key={index} event={event} />
            ))
          ) : (
            <p className="text-center w-full text-gray-500 text-lg">
              No recent event impacts found.
            </p>
          )}
        </div>
      )}
    </div>
  );
}