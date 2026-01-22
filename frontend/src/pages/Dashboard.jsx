import { useState } from "react";
import SoilForm from "../components/SoilForm";

function Dashboard() {
  const [result, setResult] = useState(null);

  return (
    <main className="container">
      <SoilForm onResult={setResult} />
    </main>
  );
}

export default Dashboard;
