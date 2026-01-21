import { useState } from "react";
import SoilForm from "../components/SoilForm";
import AnalysisResult from "../components/AnalysisResult";
import AlertBox from "../components/AlertBox";

function Dashboard() {
  const [result, setResult] = useState(null);

  return (
    <main className="container">
      <SoilForm onResult={setResult} />
      <AlertBox risk={result?.risk_level} />
      <AnalysisResult result={result} />
    </main>
  );
}

export default Dashboard;
