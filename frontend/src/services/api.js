const API_URL = import.meta.env.VITE_API_URL;

export async function analyzeSoil(payload) {
  const response = await fetch(`${API_URL}/analyze-soil`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(payload),
  });

  if (!response.ok) {
    throw new Error("API request failed");
  }

  return response.json();
}
