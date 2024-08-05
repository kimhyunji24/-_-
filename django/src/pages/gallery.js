import React, { useEffect, useState } from 'react';
import axios from 'axios';

const defaultData = [
  { id: 1, product_name: '신라면', product_img: 'shinramen.png' },
  { id: 2, product_name: '너구리', product_img: 'neoguri.png' },
  { id: 3, product_name: '불닭볶음면', product_img: 'bulldak.png' },
  { id: 4, product_name: '메로나', product_img: 'melon.png' },
  { id: 5, product_name: '코카콜라', product_img: 'cocacola.png' },
  { id: 6, product_name: '안성탕면', product_img: 'ansungtangmyun.png' },
];

function Gallery() {
  const [items, setItems] = useState(defaultData);

  useEffect(() => {
    const fetchItems = async () => {
      try {
        const response = await axios.get('/api/product/products/');
        setItems(response.data);
      } catch (error) {
        console.error('Error fetching items:', error);
        setItems(defaultData); // Fallback to default data on error
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
