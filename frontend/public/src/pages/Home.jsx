import { Card, CardContent } from "@/components/ui/card";
import { Button } from "@/components/ui/button";
import { ArrowRight } from "lucide-react";
import { Link } from "react-router-dom";
import { motion } from "framer-motion";

export default function Home() {
  return (
    <div className="w-full min-h-screen flex flex-col items-center justify-center bg-gradient-to-b from-gray-900 to-black text-white px-6 py-20">
      <motion.h1
        className="text-5xl font-bold text-center mb-6"
        initial={{ opacity: 0, y: -20 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.6 }}
      >
        AI-Powered Stock Prediction Platform
      </motion.h1>

      <motion.p
        className="text-lg text-gray-300 text-center max-w-2xl mb-10"
        initial={{ opacity: 0 }}
        animate={{ opacity: 1 }}
        transition={{ delay: 0.3, duration: 0.6 }}
      >
        Predict stock movements, assess risks, analyze event impacts, and generate
        AI-driven market narratives. All models combined in one powerful dashboard.
      </motion.p>

      <motion.div
        className="grid grid-cols-1 md:grid-cols-3 gap-6 w-full max-w-5xl"
        initial={{ opacity: 0 }}
        animate={{ opacity: 1 }}
        transition={{ delay: 0.5, duration: 0.6 }}
      >
        {/* Prediction Card */}
        <Card className="bg-gray-800 border-gray-700 hover:bg-gray-750 transition rounded-2xl">
          <CardContent className="p-6">
            <h2 className="text-xl font-semibold mb-3">Stock Prediction</h2>
            <p className="text-gray-300 mb-4">
              Generate predictions using LSTM, ARIMA, SARIMA, and LightGBM models.
            </p>
            <Link to="/predict">
              <Button className="flex items-center gap-2">Predict Now <ArrowRight size={18} /></Button>
            </Link>
          </CardContent>
        </Card>

        {/* Event Impact */}
        <Card className="bg-gray-800 border-gray-700 hover:bg-gray-750 transition rounded-2xl">
          <CardContent className="p-6">
            <h2 className="text-xl font-semibold mb-3">Event Impact</h2>
            <p className="text-gray-300 mb-4">
              Analyze how real-world events can influence stock volatility.
            </p>
            <Link to="/event-impact">
              <Button className="flex items-center gap-2">Check Impact <ArrowRight size={18} /></Button>
            </Link>
          </CardContent>
        </Card>

        {/* Risk Predictor */}
        <Card className="bg-gray-800 border-gray-700 hover:bg-gray-750 transition rounded-2xl">
          <CardContent className="p-6">
            <h2 className="text-xl font-semibold mb-3">AI Risk Predictor</h2>
            <p className="text-gray-300 mb-4">
              Get a computed risk score based on current market indicators.
            </p>
            <Link to="/risk">
              <Button className="flex items-center gap-2">View Risk <ArrowRight size={18} /></Button>
            </Link>
          </CardContent>
        </Card>
      </motion.div>

      {/* Narrative Section */}
      <motion.div
        className="w-full max-w-4xl mt-16"
        initial={{ opacity: 0 }}
        animate={{ opacity: 1 }}
        transition={{ delay: 0.6, duration: 0.6 }}
      >
        <Card className="bg-gray-800 border-gray-700 rounded-2xl p-8 text-center">
          <h2 className="text-2xl font-semibold mb-4">AI Narrative Engine</h2>
          <p className="text-gray-300 mb-6 max-w-2xl mx-auto">
            Generate human-like market explanations and trend narratives based on
            model outputs and historical data.
          </p>
          <Link to="/narrative-engine">
            <Button className="flex items-center gap-2 mx-auto">Generate Narrative <ArrowRight size={18} /></Button>
          </Link>
        </Card>
      </motion.div>
    </div>
  );
}