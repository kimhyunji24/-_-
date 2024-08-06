import React, { useState } from 'react';
import { Link } from 'react-router-dom';
import res from '../response.json'; // JSON 파일 임포트
import Modal from 'react-modal';
import '../styles/gallery.css';
import emptyHeart from '../assets/empty-heart.png'; // 빈 하트 아이콘 경로
import filledHeart from '../assets/filled-heart.png'; // 채워진 하트 아이콘 경로

function Home({ favorites, setFavorites }) {
  const [searchTerm, setSearchTerm] = useState('');
  const [hasSearched, setHasSearched] = useState(false); // 검색 상태 추가

  const handleSearch = () => {
    setHasSearched(true); // 검색 수행 상태 업데이트
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
        <Link to={`/results?search=${searchTerm}`} onClick={handleSearch}>Search</Link>
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