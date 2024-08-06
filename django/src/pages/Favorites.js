import React from 'react';
import filledHeart from '../assets/filled-heart.png'; // 채워진 하트 아이콘 경로

function Favorites({ favorites, toggleFavorite, openModalWithItem }) {
  return (
    <div>
      <h2>좋아요 목록</h2>
      {favorites.length === 0 ? (
        <p>좋아요 목록이 비어 있습니다.</p>
      ) : (
        <div className="favorites-list">
          {favorites.map(item => (
            <div key={item.id} className="favorite-item" onClick={() => openModalWithItem(item)}>
              <img src={item.product_img} alt={item.product_name} className="favorite-img" />
              <h5>{item.product_name}</h5>
              <img
                src={filledHeart}
                alt="favorite"
                onClick={(e) => {
                  e.stopPropagation(); // 클릭 이벤트가 부모에게 전달되지 않도록 함
                  toggleFavorite(item); // 즐겨찾기 해제
                }}
                className="heart-icon"
              />
            </div>
          ))}
        </div>
      )}
    </div>
  );
}

export default Favorites;
