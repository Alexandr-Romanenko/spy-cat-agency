const API_URL = "http://localhost:8000/api/";

export async function fetchCats() {
  const res = await fetch(`${API_URL}cats/`);
  if (!res.ok) throw new Error("Failed to fetch cats");
  return res.json();
}

export async function createCat(data) {
  const res = await fetch(`${API_URL}cat/create/`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(data),
  });

  if (!res.ok) {
    const errorData = await res.json().catch(() => ({}));
    console.error("Server response error:", errorData);

    let message = "Failed to create cat";
    if (typeof errorData === "object" && errorData !== null) {
      message = Object.entries(errorData)
        .map(
          ([key, val]) => `${key}: ${Array.isArray(val) ? val.join(", ") : val}`
        )
        .join("\n");
    } else if (errorData.detail) {
      message = errorData.detail;
    }
    throw new Error(message);
  }

  return res.json();
}

export async function updateCat(id, data) {
  const res = await fetch(`${API_URL}cat/${id}/update/`, {
    method: "PATCH",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(data),
  });
  if (!res.ok) throw new Error("Failed to update cat");
  return res.json();
}

export async function deleteCat(id) {
  const res = await fetch(`${API_URL}cat/${id}/delete/`, {
    method: "DELETE",
  });
  if (!res.ok) throw new Error("Failed to delete cat");
}
