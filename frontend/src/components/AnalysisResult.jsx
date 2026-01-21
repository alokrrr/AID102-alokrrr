function AnalysisResult({ result }) {
  if (!result) return null;

  return (
    <div className="card">
      <h2>AI Analysis</h2>

      <p><strong>Crop:</strong> {result.crop}</p>
      <p><strong>Soil Status:</strong> {result.soil_status}</p>

      <p className={`risk ${result.risk_level.toLowerCase()}`}>
        Risk Level: {result.risk_level}
      </p>

      <h3>Recommendations</h3>
      <ul>
        {result.recommendations.map((r, i) => (
          <li key={i}>{r}</li>
        ))}
      </ul>

      <h3>Explanation</h3>
      <p>{result.explanation}</p>
    </div>
  );
}

export default AnalysisResult;
