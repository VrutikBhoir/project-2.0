import React, { useState } from "react";
import { Mail, Phone, MapPin, Send } from "lucide-react";

export default function Contact() {
  const [form, setForm] = useState({ name: "", email: "", message: "" });
  const [sent, setSent] = useState(false);

  const handleChange = (e) => {
    setForm({ ...form, [e.target.name]: e.target.value });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    setSent(true);
    setTimeout(() => setSent(false), 3000);
  };

  return (
    <div className="min-h-screen bg-gray-50 flex justify-center items-center p-6">
      <div className="bg-white rounded-2xl shadow-lg p-8 w-full max-w-3xl">
        <h1 className="text-3xl font-bold text-center mb-6">Contact Us</h1>
        <p className="text-center text-gray-600 mb-8">
          Have questions or need support? Reach out and we’ll get back to you.
        </p>

        <div className="grid md:grid-cols-2 gap-6 mb-10">
          <div className="flex items-center gap-3">
            <Mail className="w-6 h-6" />
            <p>support@marketpulse.ai</p>
          </div>
          <div className="flex items-center gap-3">
            <Phone className="w-6 h-6" />
            <p>+91 98765 43210</p>
          </div>
          <div className="flex items-center gap-3">
            <MapPin className="w-6 h-6" />
            <p>Mumbai, India</p>
          </div>
        </div>

        <form onSubmit={handleSubmit} className="space-y-5">
          <input
            type="text"
            name="name"
            placeholder="Your Name"
            value={form.name}
            onChange={handleChange}
            className="w-full border rounded-xl p-3 focus:outline-none focus:ring"
            required
          />

          <input
            type="email"
            name="email"
            placeholder="Your Email"
            value={form.email}
            onChange={handleChange}
            className="w-full border rounded-xl p-3 focus:outline-none focus:ring"
            required
          />

          <textarea
            name="message"
            placeholder="Your Message"
            value={form.message}
            onChange={handleChange}
            rows="4"
            className="w-full border rounded-xl p-3 focus:outline-none focus:ring"
            required
          ></textarea>

          <button
            type="submit"
            className="w-full bg-blue-600 text-white py-3 rounded-xl flex justify-center items-center gap-2 hover:bg-blue-700 transition"
          >
            <Send className="w-5 h-5" /> Send Message
          </button>
        </form>

        {sent && (
          <p className="text-green-600 text-center mt-4 font-medium">
            Message sent successfully!
          </p>
        )}
      </div>
    </div>
  );
}