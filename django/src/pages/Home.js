import React, { useState } from 'react';
import axios from 'axios';

function Home() {
  const [searchTerm, setSearchTerm] = useState('');
  const [searchResults, setSearchResults] = useState([]);

  const handleSearch = async () => {
    try {
      const response = await axios.get(`/api/product/products/?search=${searchTerm}`);
      setSearchResults(response.data);
    } catch (error) {
      console.error('Error fetching search results:', error);
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
