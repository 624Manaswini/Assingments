import logo from './logo.svg';
import React, { useState } from 'react';
import axios from 'axios';
import './App.css';

function App() {
  const [query, setQuery] = useState("");
  const [result, setResult] = useState("");
  const [history, setHistory] = useState([]);
  const [showHistory, setShowHistory] = useState(false);
  const sessionId = "my-session";

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!query.trim()) return;

    try {
      const res = await axios.post("http://localhost:5000/ask", {
        user_input: query,
        session_id: sessionId
      });

      setResult(res.data.response);
      setHistory(res.data.history);
      setQuery("");
    } catch (error) {
      console.error("Error:", error);
      setResult("Something went wrong!");
    }
  };

  const handleClear = async () => {
    try {
      await axios.post("http://localhost:5000/clear", {
        session_id: sessionId
      });

      setResult("");
      setHistory([]);
    } catch (err) {
      console.error("Failed to clear history:", err);
    }
  };

  return (
    <div className="chat-container">
      <h1>Chat Buddy 🤖 </h1>

      <form onSubmit={handleSubmit}>
        <label>Query:</label>
        <input
          type="text"
          value={query}
          onChange={(e) => setQuery(e.target.value)}
          placeholder="Ask something..."
          required
        />
        <button type="submit">Submit</button>
      </form>

      <h3>Result:</h3>
      <div className="result-box">{result}</div>

      <div className="controls">
        <button onClick={() => setShowHistory(!showHistory)}>
          {showHistory ? "Hide History" : "Show History"}
        </button>
        <button onClick={handleClear} className="clear-btn">Clear History</button>
      </div>

      {showHistory && (
        <>
          <h3>History:</h3>
          <ul className="history">
            {history.map((msg, idx) => (
              <li key={idx} className={msg.role}>
                <strong>{msg.role === "user" ? "You" : "Bot"}:</strong> {msg.content}
              </li>
            ))}
          </ul>
        </>
      )}
    </div>
  );
}

export default App;
