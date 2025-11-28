import React from "react";
import { createBrowserRouter, RouterProvider } from "react-router-dom";

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

const router = createBrowserRouter([
  { path: "/", element: <Home /> },
  { path: "/predict", element: <Predict /> },
  { path: "/realtime", element: <Realtime /> },
  { path: "/compare-models", element: <CompareModels /> },
  { path: "/past-trends", element: <PastTrends /> },
  { path: "/risk", element: <RiskPredictionPage /> },
  { path: "/event-impact", element: <EventImpactPage /> },
  { path: "/narrative-engine", element: <NarrativeEnginePage /> },
  { path: "/accuracy-tracker", element: <AccuracyTrackerPage /> },
  { path: "/about", element: <About /> },
  { path: "/contact", element: <Contact /> },
  { path: "/settings", element: <Settings /> },
]);

export default function Router() {
  return <RouterProvider router={router} />;
}