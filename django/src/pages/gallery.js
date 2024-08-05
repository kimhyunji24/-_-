import React, { useEffect, useState } from 'react';
import axios from 'axios';

function Gallery() {
  const [items, setItems] = useState([]);

  useEffect(() => {
    const fetchItems = async () => {
      try {
        const response = await axios.get('/api/product/products/');
        setItems(response.data);
      } catch (error) {
        console.error('Error fetching items:', error);
      }
    };

    fetchItems();
  }, []);

  return (
    <div className="gallery-container">
      {items.map(item => (
        <div key={item.id} className="gallery-item">
          <img src={item.product_img} alt={item.product_name} />
        </div>
      ))}
    </div>
  );
}

export default Gallery;
