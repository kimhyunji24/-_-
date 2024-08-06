import React, { useState } from 'react';
import ListItem from '../components/ListItem';
import { Link } from 'react-router-dom';
import res from '../response.json'; // JSON 파일 임포트

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
        <ListItem 
          key={item.id} 
          image={item.product_img} 
          name={item.product_name} 
          nutrient={item.nutrient}
          totalScore={Math.floor(item.total_score)} // 소수점 삭제
          grade={item.grade}
        />
      ))}
      {visibleItems < favoriteResults.length && (
        <button onClick={handleLoadMore}>더보기</button>
      )}
      {favoriteResults.length === 0 && (
        <p>좋아요 한 항목이 없습니다.</p>
      )}
    </div>
  );
}

export default List;
