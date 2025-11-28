import React from "react";
import { Line } from "react-chartjs-2";
import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Legend,
} from "chart.js";

ChartJS.register(
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Legend
);

const ChartComponent = ({ labels = [], dataPoints = [], title = "Chart" }) => {
  const data = {
    labels,
    datasets: [
      {
        label: title,
        data: dataPoints,
        borderWidth: 2,
        fill: false,
      },
    ],
  };

  const options = {
    responsive: true,
    plugins: {
      legend: {
        display: true,
      },
      title: {
        display: true,
        text: title,
      },
    },
  };

  return (
    <div className="w-full h-full p-4 bg-white rounded-2xl shadow">
      <Line data={data} options={options} />
    </div>
  );
};

export default ChartComponent;