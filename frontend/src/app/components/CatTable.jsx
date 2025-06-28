"use client";

import { useState } from "react";
import { updateCat, deleteCat } from "../api";

export default function CatTable({ cats, onRefresh }) {
  const [editingId, setEditingId] = useState(null);
  const [newSalary, setNewSalary] = useState("");

  const handleUpdate = async (id) => {
    await updateCat(id, { salary: newSalary });
    setEditingId(null);
    onRefresh();
  };

  const handleDelete = async (id) => {
    await deleteCat(id);
    onRefresh();
  };

  return (
    <table className="w-full mt-6 table-auto border">
      <thead>
        <tr className="bg-gray-200">
          <th className="p-2">Name</th>
          <th>Expirience</th>
          <th>Breed</th>
          <th>Calary</th>
          <th>Actions</th>
        </tr>
      </thead>
      <tbody>
        {cats.map((cat) => (
          <tr key={cat.id} className="text-center border-t">
            <td>{cat.name}</td>
            <td>{cat.experience}</td>
            <td>{cat.breed}</td>
            <td>
              {editingId === cat.id ? (
                <input
                  type="number"
                  value={newSalary}
                  onChange={(e) => setNewSalary(e.target.value)}
                  className="border p-1 w-20"
                />
              ) : (
                cat.salary
              )}
            </td>
            <td>
              {editingId === cat.id ? (
                <button
                  className="text-green-600"
                  onClick={() => handleUpdate(cat.id)}
                >
                  Save
                </button>
              ) : (
                <button
                  className="text-blue-600"
                  onClick={() => {
                    setEditingId(cat.id);
                    setNewSalary(cat.salary);
                  }}
                >
                  Edit
                </button>
              )}
              <button
                className="text-red-600 ml-2"
                onClick={() => handleDelete(cat.id)}
              >
                Delete
              </button>
            </td>
          </tr>
        ))}
      </tbody>
    </table>
  );
}
