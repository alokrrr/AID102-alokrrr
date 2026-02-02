import DecisionTimeline from "./DecisionTimeline.jsx";
<DecisionTimeline steps={result.decision_flow} />

import PHIndicator from "./PHIndicator.jsx";
import SoilHealthBar from "./SoilHealthBar.jsx";
import NutrientChart from "./NutrientChart.jsx";

function AnalysisResult({ result }) {
  if (!result) return null;

  // Simple derived health score (explainable)
  const healthScore =
    result.risk_level === "Low" ? 80 :
    result.risk_level === "Medium" ? 55 :
    30;

  return (
    <div>
      <h2>AI Soil Analysis</h2>

      <p><strong>Crop:</strong> {result.crop}</p>
      <p><strong>Soil Status:</strong> {result.soil_status}</p>

      <span className={`risk ${result.risk_level.toLowerCase()}`}>
        {result.risk_level} Risk
      </span>

      <SoilHealthBar score={healthScore} />

      <PHIndicator
        pH={result.soil_data?.pH}
        crop={result.crop}
       />


      <NutrientChart nitrogen={result.soil_data?.nitrogen || "medium"} />

      <h3>Recommendations</h3>
      <ul>
        {result.recommendations.map((rec, i) => (
          <li key={i}>{rec}</li>
        ))}
      </ul>

      <h3>Explanation</h3>
      <p>{result.explanation}</p>
    </div>
  );
}

export default AnalysisResult;

<div style={{ marginTop: "12px" }}>
  <strong>AI Confidence:</strong>{" "}
  <span
    style={{
      color:
        result.confidence >= 0.8
          ? "#81c784"
          : result.confidence >= 0.65
          ? "#ffb74d"
          : "#e57373",
      fontWeight: "bold",
    }}
  >
    {(result.confidence * 100).toFixed(0)}%
  </span>

  <p style={{ fontSize: "0.9rem", opacity: 0.85, marginTop: "4px" }}>
    {result.confidence_reason}
  </p>
</div>
