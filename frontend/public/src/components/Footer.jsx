import React from "react";

const Footer = () => {
  return (
    <footer className="w-full py-4 bg-white shadow-inner mt-6">
      <div className="max-w-6xl mx-auto px-4 flex flex-col sm:flex-row items-center justify-between text-gray-600 text-sm">
        <p className="mb-2 sm:mb-0">© {new Date().getFullYear()} YourApp. All rights reserved.</p>

        <div className="flex gap-4">
          <a href="#" className="hover:text-black transition-colors">Privacy Policy</a>
          <a href="#" className="hover:text-black transition-colors">Terms</a>
          <a href="#" className="hover:text-black transition-colors">Support</a>
        </div>
      </div>
    </footer>
  );
};

export default Footer;