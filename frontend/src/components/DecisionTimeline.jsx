function DecisionTimeline({ steps }) {
  if (!steps || steps.length === 0) return null;

  return (
    <div style={{ marginTop: "30px" }}>
      <h3>AI Decision Timeline</h3>

      <ul style={{ marginLeft: "20px" }}>
        {steps.map((step, index) => (
          <li key={index} style={{ marginBottom: "8px" }}>
            <strong>Step {index + 1}:</strong> {step}
          </li>
        ))}
      </ul>
    </div>
  );
}

export default DecisionTimeline;
