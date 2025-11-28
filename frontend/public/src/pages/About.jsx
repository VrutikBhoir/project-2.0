import React from "react";

export default function About() {
  return (
    <div className="max-w-5xl mx-auto px-4 py-10">
      <h1 className="text-3xl font-bold mb-4 text-blue-600">About This Project</h1>

      <p className="text-gray-700 leading-relaxed mb-6">
        The Stock Price Predictor is an advanced AI-powered analytics platform designed to forecast
        stock movements, analyze market risk, interpret event impacts, and generate narrative
        explanations. It brings together machine learning models like LSTM, ARIMA, SARIMA, and
        LightGBM to help users make informed decisions.
      </p>

      <h2 className="text-2xl font-semibold mt-6 mb-2">Core Features</h2>
      <ul className="list-disc ml-6 text-gray-700 space-y-2">
        <li>📈 Real-time & historical stock predictions</li>
        <li>⚠️ AI-driven Risk Analysis using engineered indicators</li>
        <li>🎯 Event Impact Prediction for market-moving news</li>
        <li>🧠 Narrative Generation explaining market trends</li>
        <li>📊 Prediction vs Reality accuracy tracker</li>
      </ul>

      <h2 className="text-2xl font-semibold mt-6 mb-2">Technologies Used</h2>
      <ul className="list-disc ml-6 text-gray-700 space-y-2">
        <li>FastAPI for backend APIs</li>
        <li>React + TailwindCSS for frontend UI</li>
        <li>Machine Learning models (LSTM, ARIMA, LightGBM)</li>
        <li>Docker for production deployment</li>
      </ul>

      <h2 className="text-2xl font-semibold mt-6 mb-2">Goal</h2>
      <p className="text-gray-700 leading-relaxed">
        Our goal is to simplify stock analysis using AI automation and give traders, analysts, and
        learners an intelligent platform to explore and analyze market behavior with precision and ease.
      </p>
    </div>
  );
}