import logo from './logo.svg';
import './App.css';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        {/* <img src={logo} className="App-logo" alt="logo" /> */}
        <div class="logo-placeholder">
          <h1>SmartApply ✅</h1>
          <h2>Apply smarter, not harder</h2>
        </div>
        Search for a job to begin
        <div class="search-container">
          <input type="text" placeholder="Enter job title here..."></input>
          <button type="submit">Search</button>
        </div>
      </header>
      SmartApply v1.0 Alpha. Last updated on 6/23/2022.
    </div>
  );
}

export default App;
