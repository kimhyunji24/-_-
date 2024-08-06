// src/pages/List.js

import React, { useState } from 'react';
import { Link } from 'react-router-dom';
import res from '../response.json'; // JSON 파일 임포트
import '../styles/list.css'; // 스타일 파일 임포트

const ITEMS_PER_PAGE = 5; // 한 번에 보여줄 항목 수

function List({ favorites }) {
  const [visibleItems, setVisibleItems] = useState(ITEMS_PER_PAGE);

  const handleLoadMore = () => {
    setVisibleItems(prevVisibleItems => prevVisibleItems + ITEMS_PER_PAGE);
  };

  // grade가 "Z"인 항목을 제외하도록 필터링
  const filteredResults = res.results.filter(item => item.grade !== 'Z');

  // 좋아요된 항목을 필터링
  const favoriteResults = filteredResults.filter(item =>
    favorites.some(fav => fav.id === item.id)
  );

  return (
    <div className="list-container">
      <h2>좋아요 목록</h2>
      <Link to="/">홈으로 돌아가기</Link>
      {favoriteResults.slice(0, visibleItems).map(item => (
        <div key={item.id} className="list-item-container">
          <img src={item.product_img} alt={item.product_name} className="list-item-image" />
          <div className="list-item-details">
            <h3>{item.product_name}</h3>
            <p><strong>Nutrient Information:</strong> {item.nutrient}</p>
            <p><strong>Total Score:</strong> {Math.floor(item.total_score)}</p>
            <p><strong>Grade:</strong> {item.grade}</p>
          </div>
        </div>
      ))}
      {visibleItems < favoriteResults.length && (
        <button onClick={handleLoadMore} className="load-more-button">더보기</button>
      )}
      {favoriteResults.length === 0 && (
        <p>좋아요 한 항목이 없습니다.</p>
      )}
    </div>
  );
}

export default List;
