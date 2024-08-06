import React, { useState } from 'react';
import ListItem from '../components/ListItem';
import res from '../response.json'; // JSON 파일 임포트

const ITEMS_PER_PAGE = 5; // 한 번에 보여줄 항목 수

function List() {
  const [visibleItems, setVisibleItems] = useState(ITEMS_PER_PAGE);

  const handleLoadMore = () => {
    setVisibleItems(prevVisibleItems => prevVisibleItems + ITEMS_PER_PAGE);
  };

  // grade가 "Z"인 항목을 제외하도록 필터링
  const filteredResults = res.results.filter(item => item.grade !== 'Z');

  return (
    <div className="list-container">
      {filteredResults.slice(0, visibleItems).map(item => (
        <ListItem 
          key={item.id} 
          image={item.product_img} 
          name={item.product_name} 
          nutrient={item.nutrient}
          totalScore={Math.floor(item.total_score)} // 소수점 삭제
          grade={item.grade}
        />
      ))}
      {visibleItems < filteredResults.length && (
        <button onClick={handleLoadMore}>더보기</button>
      )}
    </div>
  );
}

export default List;
