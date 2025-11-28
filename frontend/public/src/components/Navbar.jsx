import { Link } from "react-router-dom";
import { Menu, X } from "lucide-react";
import { useState } from "react";

export default function Navbar() {
  const [open, setOpen] = useState(false);

  return (
    <nav className="w-full bg-white shadow-md fixed top-0 left-0 z-50">
      <div className="max-w-7xl mx-auto px-4 py-3 flex items-center justify-between">
        {/* Logo */}
        <Link to="/" className="text-2xl font-bold text-blue-600">
          StockPredictor
        </Link>

        {/* Desktop Menu */}
        <div className="hidden md:flex items-center gap-6 text-gray-700 font-medium">
          <Link to="/predict" className="hover:text-blue-600">Predict</Link>
          <Link to="/realtime" className="hover:text-blue-600">Realtime</Link>
          <Link to="/compare-models" className="hover:text-blue-600">Compare Models</Link>
          <Link to="/past-trends" className="hover:text-blue-600">Past Trends</Link>
          <Link to="/risk" className="hover:text-blue-600">Risk</Link>
          <Link to="/event-impact" className="hover:text-blue-600">Event Impact</Link>
          <Link to="/narrative" className="hover:text-blue-600">Narrative</Link>
          <Link to="/accuracy" className="hover:text-blue-600">Tracker</Link>
          <Link to="/about" className="hover:text-blue-600">About</Link>
          <Link to="/contact" className="hover:text-blue-600">Contact</Link>
        </div>

        {/* Mobile Menu Button */}
        <button
          className="md:hidden"
          onClick={() => setOpen(!open)}
        >
          {open ? <X size={26} /> : <Menu size={26} />}
        </button>
      </div>

      {/* Mobile Dropdown */}
      {open && (
        <div className="md:hidden bg-white shadow-md px-4 pb-4 flex flex-col gap-3 text-gray-700 font-medium">
          <Link to="/predict" onClick={() => setOpen(false)}>Predict</Link>
          <Link to="/realtime" onClick={() => setOpen(false)}>Realtime</Link>
          <Link to="/compare-models" onClick={() => setOpen(false)}>Compare Models</Link>
          <Link to="/past-trends" onClick={() => setOpen(false)}>Past Trends</Link>
          <Link to="/risk" onClick={() => setOpen(false)}>Risk</Link>
          <Link to="/event-impact" onClick={() => setOpen(false)}>Event Impact</Link>
          <Link to="/narrative" onClick={() => setOpen(false)}>Narrative</Link>
          <Link to="/accuracy" onClick={() => setOpen(false)}>Tracker</Link>
          <Link to="/about" onClick={() => setOpen(false)}>About</Link>
          <Link to="/contact" onClick={() => setOpen(false)}>Contact</Link>
        </div>
      )}
    </nav>
  );
}