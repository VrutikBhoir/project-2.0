import React from "react";
import { Card, CardContent } from "@/components/ui/card";
import { ArrowUpRight, ArrowDownRight, Dot } from "lucide-react";

const EventImpactCard = ({
  title = "Event Title",
  impact = 0,
  severity = "Low",
  timestamp = "--",
}) => {
  const getSeverityColor = () => {
    switch (severity) {
      case "High":
        return "text-red-600";
      case "Medium":
        return "text-yellow-600";
      default:
        return "text-green-600";
    }
  };

  return (
    <Card className="rounded-2xl shadow p-4 bg-white hover:shadow-lg transition-all cursor-pointer">
      <CardContent className="p-0">
        <div className="flex items-center justify-between mb-2">
          <h2 className="text-lg font-semibold">{title}</h2>
          <span
            className={`px-3 py-1 text-sm rounded-full font-medium ${getSeverityColor()} bg-opacity-10`}
          >
            {severity}
          </span>
        </div>

        <div className="flex items-center gap-2 text-sm text-gray-600 mb-3">
          <Dot />
          <p>{timestamp}</p>
        </div>

        <div className="flex items-center justify-between mt-4">
          <p className="text-gray-700 font-medium">Impact Score:</p>

          <div className="flex items-center gap-1 text-lg font-bold">
            {impact >= 0 ? (
              <ArrowUpRight className="w-5 h-5 text-green-600" />
            ) : (
              <ArrowDownRight className="w-5 h-5 text-red-600" />
            )}
            <span>{impact}</span>
          </div>
        </div>
      </CardContent>
    </Card>
  );
};

export default EventImpactCard;