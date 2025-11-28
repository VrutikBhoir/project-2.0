import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Navbar from "./components/Navbar";
import Footer from "./components/Footer";

import Home from "./pages/Home";
import Predict from "./pages/Predict";
import Realtime from "./pages/Realtime";
import CompareModels from "./pages/CompareModels";
import PastTrends from "./pages/PastTrends";
import RiskPredictionPage from "./pages/RiskPredictionPage";
import EventImpactPage from "./pages/EventImpactPage";
import NarrativeEnginePage from "./pages/NarrativeEnginePage";
import AccuracyTrackerPage from "./pages/AccuracyTrackerPage";
import About from "./pages/About";
import Contact from "./pages/Contact";
import Settings from "./pages/Settings";

export default function App() {
  return (
    <Router>
      <Navbar />
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/predict" element={<Predict />} />
        <Route path="/realtime" element={<Realtime />} />
        <Route path="/compare-models" element={<CompareModels />} />
        <Route path="/past-trends" element={<PastTrends />} />
        <Route path="/risk" element={<RiskPredictionPage />} />
        <Route path="/event-impact" element={<EventImpactPage />} />
        <Route path="/narrative-engine" element={<NarrativeEnginePage />} />
        <Route path="/accuracy-tracker" element={<AccuracyTrackerPage />} />
        <Route path="/about" element={<About />} />
        <Route path="/contact" element={<Contact />} />
        <Route path="/settings" element={<Settings />} />
      </Routes>
      <Footer />
    </Router>
  );
}
