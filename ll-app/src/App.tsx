import { useState } from 'react';
import { invoke } from '@tauri-apps/api/tauri';
import './App.css'; // We'll create and import the CSS file next

function App() {
  // --- React State Management (`useState`) ---
  // State for the text in the textarea
  const [inputText, setInputText] = useState<string>('');
  
  // State to hold the array of words and spaces for rendering
  const [words, setWords] = useState<string[]>([]);
  
  // State for the backend connection status message
  const [pingStatus, setPingStatus] = useState<{ message: string; color: string }>({
    message: 'Idle',
    color: '#333',
  });

  // --- Logic Functions (Event Handlers) ---

  /**
   * (Day 3) Processes the input text and stores it in the `words` state.
   * React will automatically re-render the UI when this state changes.
   */
  const handleReadText = () => {
    if (!inputText.trim()) {
      setWords([]); // Clear the reader view if input is empty
      return;
    }
    // Split text but keep whitespace to preserve formatting like newlines
    const processedWords = inputText.split(/(\s+)/);
    setWords(processedWords);
  };

  /**
   * (Day 5) Pings the Rust backend and updates the UI based on the response.
   */
  const testBackendConnection = async () => {
    setPingStatus({ message: 'Pinging...', color: '#f39c12' }); // Orange

    try {
      // The generic <string> tells TypeScript what to expect from Rust.
      const response = await invoke<string>('ping');
      setPingStatus({ message: `Success! Received: "${response}"`, color: '#2ecc71' }); // Green
      console.log('Ping response:', response);
    } catch (error) {
      setPingStatus({ message: 'Failed to connect.', color: '#e74c3c' }); // Red
      console.error('Ping error:', error);
    }
  };

  // --- Rendered UI (JSX) ---
  // This is the declarative way to define what the UI should look like.
  return (
    <div className="container">
      <h1>Language Learning App</h1>

      {/* Section for user input */}
      <div className="input-area">
        <textarea
          rows={10}
          placeholder="Paste your text here..."
          value={inputText}
          onChange={(e) => setInputText(e.target.value)}
        />
        <button onClick={handleReadText}>Read Text</button>
      </div>

      <hr />

      {/* The main reader view where interactive text will be displayed */}
      <h2>Reader View</h2>
      <div className="reader-view-panel">
        {words.length > 0 ? (
          // Map over the `words` state array to render each word
          words.map((word, index) =>
            // Use a <span> for words and a <React.Fragment> for whitespace
            word.match(/^\s+$/) ? (
              <span key={index}>{word.replace(/\n/g, '<br />')}</span>
            ) : (
              <span key={index} className="word">
                {word}
              </span>
            )
          )
        ) : (
          <p className="placeholder">Your text will appear here once you submit it.</p>
        )}
      </div>

      {/* Section for testing backend connection */}
      <div className="connection-test">
        <button onClick={testBackendConnection}>Test Backend Connection</button>
        <p>
          Status: <span style={{ color: pingStatus.color, fontWeight: 'bold' }}>{pingStatus.message}</span>
        </p>
      </div>
    </div>
  );
}

export default App;