import React, { useState } from "react";
import axios from "axios";
import "./App.css";

function App() {
  const [ticker, setTicker] = useState("");
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const getMarketPulse = async () => {
    if (!ticker) return;
    setLoading(true);
    setError(null);
    setResult(null);

    try {
const response = await axios.get(`http://localhost:8000/api/v1/market-pulse?ticker=${ticker}`);
      setResult(response.data);
    } catch (err) {
      setError("Error fetching data. Please try again.");
    }
    setLoading(false);
  };

  return (
    <div className="App">
      <h1>📈 Market Pulse</h1>
      <input
        type="text"
        placeholder="Enter stock ticker (e.g. AAPL)"
        value={ticker}
        onChange={(e) => setTicker(e.target.value)}
      />
      <button onClick={getMarketPulse}>Get Pulse</button>

      {loading && <p>Loading...</p>}
      {error && <p className="error">{error}</p>}

      {result && (
        <div className="result">
          <h2>{result.ticker}</h2>
          <p><strong>Pulse:</strong> {result.pulse.toUpperCase()}</p>
          <p><strong>Explanation:</strong> {result.llm_explanation}</p>
          <details>
            <summary>🔍 Show full JSON</summary>
            <pre>{JSON.stringify(result, null, 2)}</pre>
          </details>
        </div>
      )}
    </div>
  );
}

export default App;