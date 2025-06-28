"use client";

import { useState } from "react";
import { createCat } from "../api";

export default function CatForm({ onSuccess }) {
  const [form, setForm] = useState({
    name: "",
    experience: "",
    breed: "",
    salary: "",
  });

  const [error, setError] = useState("");

  const handleChange = (e) => {
    setForm({ ...form, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError("");

    if (
      !form.name.trim() ||
      !form.breed.trim() ||
      !form.experience.trim() ||
      !form.salary.trim()
    ) {
      setError("Please fill all fields");
      return;
    }

    const experience = parseInt(form.experience);
    const salary = parseFloat(form.salary);

    if (isNaN(experience) || isNaN(salary)) {
      setError("Experience and salary must be valid numbers");
      return;
    }

    try {
      await createCat({
        name: form.name.trim(),
        breed: form.breed.trim(),
        experience,
        salary,
      });
      setForm({ name: "", experience: "", breed: "", salary: "" });
      if (onSuccess) onSuccess();
    } catch (err) {
      console.error(err);
      setError("Error when creating a cat: " + err.message);
    }
  };

  return (
    <form
      onSubmit={handleSubmit}
      className="space-y-4 bg-gray-100 p-4 rounded shadow"
    >
      <h2 className="text-xl font-semibold">Add cat</h2>

      <input
        name="name"
        placeholder="Name"
        value={form.name}
        onChange={handleChange}
        className="w-full border p-2 rounded"
      />

      <input
        name="experience"
        placeholder="Experience (full years)"
        value={form.experience}
        onChange={handleChange}
        className="w-full border p-2 rounded"
      />

      <input
        name="breed"
        placeholder="Breed"
        value={form.breed}
        onChange={handleChange}
        className="w-full border p-2 rounded"
      />

      <input
        name="salary"
        placeholder="Salary"
        value={form.salary}
        onChange={handleChange}
        className="w-full border p-2 rounded"
      />

      {error && (
        <div className="text-red-600 whitespace-pre-line mb-2">{error}</div>
      )}

      <button
        type="submit"
        className="bg-blue-600 text-white px-4 py-2 rounded"
      >
        Create
      </button>
    </form>
  );
}
