import logo from './logo.svg';
import './App.css';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        Search for a job to begin
        <input type="text" placeholder="Enter job title here..."></input>
        <button type="submit">Search</button>
      </header>
      SmartApply v1.0 Alpha. Last updated on 6/20/2022.
    </div>
  );
}

export default App;
