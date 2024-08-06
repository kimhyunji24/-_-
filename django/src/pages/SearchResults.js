
import React, { useEffect, useState } from 'react';
import { useLocation } from 'react-router-dom';
import Modal from 'react-modal';
import res from '../response.json'; // JSON 파일 임포트
import emptyHeart from '../assets/empty-heart.png'; // 빈 하트 아이콘 경로
import filledHeart from '../assets/filled-heart.png'; // 채워진 하트 아이콘 경로

Modal.setAppElement('#root'); // Modal root 설정

function SearchResults({ favorites, toggleFavorite }) {
  const location = useLocation();
  const [results, setResults] = useState([]);
  const [modalIsOpen, setModalIsOpen] = useState(false);
  const [selectedItem, setSelectedItem] = useState(null);

  useEffect(() => {
    const query = new URLSearchParams(location.search);
    const searchTerm = query.get('search')?.toLowerCase();

    if (searchTerm) {
      const filteredResults = res.results.filter(item =>
        item.product_name.toLowerCase().includes(searchTerm)
      );
      setResults(filteredResults);
    }
  }, [location]);

  // openModalWithItem 함수 정의
  const openModalWithItem = (item) => {
    setSelectedItem(item);
    setModalIsOpen(true);
  };

  const closeModal = () => {
    setModalIsOpen(false);
    setSelectedItem(null);
  };

  return (
    <div>
      {results.length > 0 ? (
        <div>
          <h4>검색 결과</h4>
          <div className="similar-results">
            {results.map(item => (
              <div key={item.id} className="similar-item" onClick={() => openModalWithItem(item)}>
                <img src={item.product_img} alt={item.product_name} className="search-result-img" />
                <h5>{item.product_name}</h5>
                <img
                  src={favorites.some(fav => fav.id === item.id) ? filledHeart : emptyHeart}
                  alt="favorite"
                  onClick={(e) => {
                    e.stopPropagation(); // 클릭 이벤트가 부모에게 전달되지 않도록 함
                    toggleFavorite(item); // 즐겨찾기 추가/제거
                  }}
                  className="heart-icon"
                />
              </div>
            ))}
          </div>
        </div>
      ) : (
        <p>검색 결과가 없습니다.</p>
      )}

      {/* Modal */}
      {selectedItem && (
        <Modal
          isOpen={modalIsOpen}
          onRequestClose={closeModal}
          contentLabel="Item Details"
          className="modal"
          overlayClassName="overlay"
        >
          <div className="modal-content">
            <img src={selectedItem.product_img} alt={selectedItem.product_name} />
            <h3>{selectedItem.product_name}</h3>
            <p><strong>Ingredients:</strong> {selectedItem.ingredient}</p>
            <p><strong>Nutrient Information:</strong> {selectedItem.nutrient}</p>
            <p><strong>Grade: </strong>{selectedItem.grade}</p>

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
    </div>
  );
}

export default SearchResults;