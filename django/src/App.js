
import React , { useState } from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Header from './components/Header';
import Home from './pages/Home';
import List from './pages/List';
import Footer from './components/Footer';
import SearchResults from './pages/SearchResults';

function App() {
  const [favorites, setFavorites] = useState([]); // 상태 정의

  return (
    <Router>
      <Header />
      <div>
        <Routes>
          <Route path="/" element={<Home favorites={favorites} setFavorites={setFavorites} />} />
          <Route path="/favorites" element={<List favorites={favorites} />} />
          <Route path="/search" element={<SearchResults favorites={favorites} setFavorites={setFavorites} />} />
        </Routes>
        <Footer />
      </div>
    </Router>
  );
}

export default App;