"use client";

import { useEffect, useState } from "react";
import { fetchCats } from "./api";
import CatForm from "../app/components/CatForm";
import CatTable from "../app/components/CatTable";

export default function HomePage() {
  const [cats, setCats] = useState([]);

  const loadCats = async () => {
    try {
      const data = await fetchCats();
      setCats(data);
    } catch (err) {
      console.error("Error loading cats:", err);
    }
  };

  useEffect(() => {
    loadCats();
  }, []);

  return (
    <main className="p-8 max-w-4xl mx-auto">
      <h1 className="text-3xl font-bold mb-6">Spy Cats Dashboard</h1>
      <CatForm onSuccess={loadCats} />
      <CatTable cats={cats} onRefresh={loadCats} />
    </main>
  );
}
