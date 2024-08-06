import React, { useState } from 'react';
import { Link } from 'react-router-dom';
import res from '../response.json'; // JSON 파일 임포트
import Modal from 'react-modal';
import '../styles/gallery.css';
import emptyHeart from '../assets/empty-heart.png'; // 빈 하트 아이콘 경로
import filledHeart from '../assets/filled-heart.png'; // 채워진 하트 아이콘 경로

Modal.setAppElement('#root'); // Modal root 설정

function Home({ favorites, setFavorites }) {
  const [searchTerm, setSearchTerm] = useState('');
  const [searchResults, setSearchResults] = useState([]);
  const [similarResults, setSimilarResults] = useState([]);
  const [modalIsOpen, setModalIsOpen] = useState(false);
  const [selectedItem, setSelectedItem] = useState(null);
  const [hasSearched, setHasSearched] = useState(false); // 검색 상태 추가

  const handleSearch = () => {
    setHasSearched(true); // 검색 수행 상태 업데이트

    const lowerCaseSearchTerm = searchTerm.toLowerCase();
    const results = res.results.filter(item =>
      item.product_name.toLowerCase() === lowerCaseSearchTerm
    );
    setSearchResults(results);

    if (results.length > 0) {
      setSelectedItem(results[0]);
      setModalIsOpen(true);
      setSimilarResults([]);
    } else {
      setModalIsOpen(false);
      setSelectedItem(null);
      const similar = res.results.filter(item =>
        item.product_name.toLowerCase().includes(lowerCaseSearchTerm)
      );
      setSimilarResults(similar);
    }
  };

  const openModalWithItem = (item) => {
    setSelectedItem(item);
    setModalIsOpen(true);
  };

  const closeModal = () => {
    setModalIsOpen(false);
    setSelectedItem(null);
  };

  const toggleFavorite = (item) => {
    setFavorites((prevFavorites) => {
      if (prevFavorites.some(fav => fav.id === item.id)) {
        return prevFavorites.filter(fav => fav.id !== item.id);
      } else {
        return [...prevFavorites, item];
      }
    });
  };

  return (
    <div>
      <div className="search-bar">
        <input
          type="text"
          placeholder="Search for any food"
          value={searchTerm}
          onChange={(e) => setSearchTerm(e.target.value)}
        />
        <button onClick={handleSearch}>Search</button>
      </div>

      {selectedItem && (
        <Modal
          isOpen={modalIsOpen}
          onRequestClose={closeModal}
          contentLabel="Search Result"
          className="modal"
          overlayClassName="overlay"
        >
          <div className="modal-content">
            <img src={selectedItem.product_img} alt={selectedItem.product_name} />
            <h3>{selectedItem.product_name}</h3>
            <p><strong>Ingredients:</strong> {selectedItem.ingredient}</p>
            <p><strong>Nutrient Information:</strong> {selectedItem.nutrient}</p>
            <img
              src={favorites.some(fav => fav.id === selectedItem.id) ? filledHeart : emptyHeart}
              alt="favorite"
              onClick={() => toggleFavorite(selectedItem)}
              className="heart-icon"
            />
            <button onClick={closeModal}>Close</button>
          </div>
        </Modal>
      )}

      {/* 검색 후 검색 결과가 없을 때만 "검색 결과가 없습니다" 메시지를 표시 */}
      {hasSearched && searchResults.length === 0 && similarResults.length === 0 && (
        <p>검색 결과가 없습니다.</p>
      )}

      {similarResults.length > 0 && (
        <div>
          <h4>검색 결과</h4>
          <div className="similar-results">
            {similarResults.map(item => (
              <div key={item.id} className="similar-item" onClick={() => openModalWithItem(item)}>
                <img src={item.product_img} alt={item.product_name} />
                <h5>{item.product_name}</h5>
                <img
                  src={favorites.some(fav => fav.id === item.id) ? filledHeart : emptyHeart}
                  alt="favorite"
                  onClick={(e) => { e.stopPropagation(); toggleFavorite(item); }}
                  className="heart-icon"
                />
              </div>
            ))}
          </div>
        </div>
      )}

      <Link to="/favorites">좋아요 목록 보기</Link>
    </div>
  );
}

export default Home;
