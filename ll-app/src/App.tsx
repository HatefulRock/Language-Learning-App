// src/App.tsx
import React, { useState, useEffect } from 'react';
import { invoke } from '@tauri-apps/api/tauri';
import './App.css';

function App() {
  const [greeting, setGreeting] = useState('');

  useEffect(() => {
    invoke<string>('greet', { name: 'World' })
      .then(result => setGreeting(result))
      .catch(console.error);
  }, []);

  return (
    <div className="container">
      <h1>Welcome to Tauri!</h1>
      <p>{greeting}</p>
    </div>
  );
}

export default App;