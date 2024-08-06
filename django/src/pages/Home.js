import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom'; // useNavigate 훅 사용
import res from '../response.json'; // JSON 파일 임포트
import '../styles/gallery.css';

function Home({ favorites, setFavorites }) {
  const [searchTerm, setSearchTerm] = useState('');
  const [hasSearched, setHasSearched] = useState(false); // 검색 상태 추가
  const navigate = useNavigate(); // useNavigate 훅 사용

  const handleSearch = () => {
    setHasSearched(true); // 검색 수행 상태 업데이트
    navigate(`/results?search=${searchTerm}`); // 결과 페이지로 이동
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
        <button onClick={handleSearch} className="search-button">Search</button> {/* 버튼으로 변경 */}
      </div>

      {/* 검색 후 검색 결과가 없을 때만 "검색 결과가 없습니다" 메시지를 표시 */}
      {hasSearched && (
        <p>검색 결과가 없습니다.</p>
      )}

      {/* <Link to="/favorites">좋아요 목록 보기</Link> */}
    </div>
  );
}

export default Home;
