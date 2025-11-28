import React, { useState } from "react";

export default function Settings() {
  const [theme, setTheme] = useState("light");
  const [refreshInterval, setRefreshInterval] = useState(10);

  const handleThemeChange = (e) => setTheme(e.target.value);
  const handleIntervalChange = (e) => setRefreshInterval(Number(e.target.value));

  const saveSettings = () => {
    localStorage.setItem("theme", theme);
    localStorage.setItem("refreshInterval", refreshInterval);
    alert("Settings saved!");
  };

  return (
    <div className="min-h-screen bg-gray-50 p-6">
      <h1 className="text-3xl font-bold text-center mb-6">Settings</h1>

      <div className="max-w-md mx-auto space-y-6 bg-white p-6 rounded-2xl shadow">
        <div>
          <label className="block font-medium mb-2">Theme</label>
          <select
            value={theme}
            onChange={handleThemeChange}
            className="w-full p-3 border rounded-xl focus:ring focus:ring-blue-300"
          >
            <option value="light">Light</option>
            <option value="dark">Dark</option>
          </select>
        </div>

        <div>
          <label className="block font-medium mb-2">Realtime Refresh Interval (seconds)</label>
          <input
            type="number"
            value={refreshInterval}
            onChange={handleIntervalChange}
            min={1}
            className="w-full p-3 border rounded-xl focus:ring focus:ring-blue-300"
          />
        </div>

        <button
          onClick={saveSettings}
          className="w-full py-3 bg-blue-600 text-white rounded-xl hover:bg-blue-700 transition"
        >
          Save Settings
        </button>
      </div>
    </div>
  );
}