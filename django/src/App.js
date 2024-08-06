import React, { useState } from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Header from './components/Header';
import Home from './pages/Home';
import List from './pages/List';
import Footer from './components/Footer';
import Favorites from './components/Favorites';
import SearchResults from './pages/SearchResults'; // SearchResults 컴포넌트 추가


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
      <div>
        <Header />
        <Routes>
          <Route path="/" element={<Home favorites={favorites} setFavorites={setFavorites} />} />
          <Route path="/results" element={<SearchResults favorites={favorites} toggleFavorite={toggleFavorite} openModalWithItem={() => {}} />} /> {/* toggleFavorite 함수 전달 */}
          <Route path="/favorites" element={<Favorites favorites={favorites} toggleFavorite={toggleFavorite} openModalWithItem={() => {}} />} />
        </Routes>
        <Footer />
      </div>
    </Router>
  );
}

export default App;
