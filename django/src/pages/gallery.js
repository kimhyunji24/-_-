import React, { useEffect, useState } from 'react';
import axios from 'axios';
import Header from '../components/Header';
import Footer from '../components/Footer';

function Gallery() {
  const [items, setItems] = useState([]);

  useEffect(() => {
    const fetchItems = async () => {
      try {
        // const response = await axios.get('http://localhost:8000/api/items/');
        setItems(response.data);
      } catch (error) {
        console.error('Error fetching items:', error);
      }
    };

    fetchItems();
  }, []);

  return (
    <div>
      <Header />
      <div className="search-bar">
        <input type="text" placeholder="Search for any food" />
        <button>Search</button>
      </div>
      <div className="gallery-container">
        {items.map(item => (
          <div key={item.id} className="gallery-item">
            <img src={item.image} alt={item.name} />
          </div>
        ))}
      </div>
      <Footer />
    </div>
  );
}

export default Gallery;

