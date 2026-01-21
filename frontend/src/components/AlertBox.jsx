function AlertBox({ risk }) {
  if (!risk || risk === "Low") return null;

  return (
    <div className={`alert ${risk.toLowerCase()}`}>
      ⚠ {risk} priority soil alert detected
    </div>
  );
}

export default AlertBox;
