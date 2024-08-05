import React, { useState } from 'react';
import axios from 'axios';

const defaultData = [
  { id: 1, product_name: '신라면', ingredient: '성분1, 성분2, 성분3', product_img: 'shinramen.png' },
  { id: 2, product_name: '너구리', ingredient: '성분1, 성분2, 성분3', product_img: 'neoguri.png' },
  { id: 3, product_name: '메로나', ingredient: '성분1, 성분2, 성분3', product_img: 'melon.png' },
  { id: 4, product_name: '홈런볼', ingredient: '성분1, 성분2, 성분3', product_img: 'homerun.png' },
];

function Home() {
  const [searchTerm, setSearchTerm] = useState('');
  const [searchResults, setSearchResults] = useState(defaultData);

  const handleSearch = async () => {
    try {
      const response = await axios.get(`/api/product/products/?search=${searchTerm}`);
      setSearchResults(response.data);
    } catch (error) {
      console.error('Error fetching search results:', error);
      setSearchResults(defaultData); // Fallback to default data on error
    }
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
      <div className="gallery-container">
        {searchResults.map((item) => (
          <div key={item.id} className="gallery-item">
            <img src={item.product_img} alt={item.product_name} />
            <div>
              <h3>{item.product_name}</h3>
              <p>{item.ingredient}</p>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}

export default Home;
