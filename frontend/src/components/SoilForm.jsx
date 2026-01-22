import { useState } from "react";
import { analyzeSoil } from "../services/api";

function SoilForm({ onResult }) {
  const [crop, setCrop] = useState("wheat");
  const [pH, setPH] = useState("");
  const [nitrogen, setNitrogen] = useState("medium");
  const [potassium, setPotassium] = useState("medium");
  const [loading, setLoading] = useState(false);

  async function handleSubmit(e) {
    e.preventDefault();
    setLoading(true);

    const payload = {
      crop,
      soil_data: {
        pH: Number(pH),
        nitrogen,
        ...(crop !== "wheat" && { potassium }),
      },
    };

    try {
      const response = await analyzeSoil(payload);
      onResult(response.analysis);
    } catch (err) {
      alert(err.message);
    } finally {
      setLoading(false);
    }
  }

  return (
    <form className="card" onSubmit={handleSubmit}>
      <h2>Soil Input</h2>

      <label>Crop</label>
      <select value={crop} onChange={(e) => setCrop(e.target.value)}>
        <option value="wheat">Wheat</option>
        <option value="rice">Rice</option>
        <option value="cotton">Cotton</option>
      </select>

      <label>Soil pH</label>
      <input
        type="number"
        step="0.1"
        required
        value={pH}
        onChange={(e) => setPH(e.target.value)}
      />

      <label>Nitrogen Level</label>
      <select
        value={nitrogen}
        onChange={(e) => setNitrogen(e.target.value)}
      >
        <option value="low">Low</option>
        <option value="medium">Medium</option>
        <option value="high">High</option>
      </select>

      {crop !== "wheat" && (
        <>
          <label>Potassium Level</label>
          <select
            value={potassium}
            onChange={(e) => setPotassium(e.target.value)}
          >
            <option value="low">Low</option>
            <option value="medium">Medium</option>
            <option value="high">High</option>
          </select>
        </>
      )}

      <button type="submit" disabled={loading}>
        {loading ? "Analyzing..." : "Analyze Soil"}
      </button>
    </form>
  );
}

export default SoilForm;
