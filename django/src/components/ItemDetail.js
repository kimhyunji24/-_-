import React from 'react';
import { useParams } from 'react-router-dom';

function ItemDetail() {
  const { name } = useParams();

  // 여기서 name을 사용하여 DB에서 해당 항목의 세부 정보
  // 예시로 단순히 name을 
  return (
    <div>
      <h2>{name} 상세 페이지</h2>
      <p>여기에 {name}에 대한 세부 정보를 표시.</p>
    </div>
  );
}

export default ItemDetail;
