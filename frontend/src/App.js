import logo from './logo.svg';
import './App.css';
import Home from './Home';
import Results from './results';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';

function App() {
  return (
    <Router>
      <Routes>
        <Route exact path='/' element={<Home />} />
        <Route exact path='/search' element={<Results />} />
      </Routes>
    </Router>
  );
}

export default App;
