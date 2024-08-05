import React from 'react';

function ListItem({ image, name, ingredients }) {
  return (
    <div className="list-item">
      <img src={image} alt={name} />
      <div className="item-info">
        <h3>{name}</h3>
        <p>{ingredients}</p>
        <div className="actions">
          <span>❤️</span>
          <button>Read More</button>
        </div>
      </div>
    </div>
  );
}

export default ListItem;
