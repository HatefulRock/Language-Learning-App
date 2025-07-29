import { useState } from 'react';
import { invoke } from '@tauri-apps/api/tauri';
import './App.css';

function App() {
  const [greeting, setGreeting] = useState('');

  const callRust = async () => {
    // Invoke the 'greet' command from the Rust backend
    const result: string = await invoke('greet', { name: 'World' });
    setGreeting(result);
  };

  return (
    <div className="container">
      <h1>Welcome to Your Language Learning App!</h1>
      <p>This is the starting point of your Tauri + React application.</p>
      
      <button onClick={callRust}>Call Rust Backend</button>
      
      {greeting && <p>{greeting}</p>}
    </div>
  );
}

export default App;