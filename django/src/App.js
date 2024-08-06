import React, { useState } from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Header from './components/Header';
import Home from './pages/Home';
import Favorites from './pages/Favorites';
import Footer from './components/Footer';
import SearchResults from './pages/SearchResults';

function App() {
  const [favorites, setFavorites] = useState([]);

  const toggleFavorite = (item) => {
    setFavorites((prevFavorites) => {
      if (prevFavorites.some(fav => fav.id === item.id)) {
        return prevFavorites.filter(fav => fav.id !== item.id); // 즐겨찾기 제거
      } else {
        return [...prevFavorites, item]; // 즐겨찾기 추가
      }
    });
  };

  return (
    <Router>
      <Header />
      <Routes>
        <Route path="/" element={<Home favorites={favorites} setFavorites={setFavorites} />} />
        <Route path="/results" element={<SearchResults favorites={favorites} toggleFavorite={toggleFavorite} />} />
        <Route path="/favorites" element={<Favorites favorites={favorites} toggleFavorite={toggleFavorite} />} />
      </Routes>
      <Footer />
    </Router>
  );
}

export default App;
