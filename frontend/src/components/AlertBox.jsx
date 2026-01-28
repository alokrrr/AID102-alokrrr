function AlertBox({ alerts }) {
  if (!alerts || alerts.length === 0) return null;

  return (
    <div style={{ marginBottom: "20px" }}>
      {alerts.map((alert, index) => (
        <div
          key={index}
          className={`alert ${alert.severity.toLowerCase()}`}
        >
          <strong>{alert.type}:</strong> {alert.message}
        </div>
      ))}
    </div>
  );
}

export default AlertBox;
