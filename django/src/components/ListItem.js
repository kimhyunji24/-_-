import React, { useState } from 'react';

function ListItem({ image, name, nutrient, totalScore, grade }) {
  const [liked, setLiked] = useState(false);

  const handleLike = () => {
    setLiked(!liked);
  };

  return (
    <div className="list-item">
      <img src={image} alt={name} />
      <div className="item-info">
        <h3>{name}</h3>
        <p><strong>Nutrient Information:</strong>{nutrient}</p>
        <p><strong>Total Score:</strong> {totalScore}</p>
        <p><strong>Grade:</strong> {grade}</p>
        <div className="actions">
          <span onClick={handleLike}>
            {liked ? '❤️' : '🤍'}
          </span>
          <button>Read More</button>
        </div>
      </div>
    </div>
  );
}

export default ListItem;
