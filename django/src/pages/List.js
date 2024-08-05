import React from 'react';
import ListItem from '../components/ListItem';

const defaultData = [
  { id: 1, product_name: '신라면', ingredient: '성분1, 성분2, 성분3', product_img: 'shinramen.png' },
  { id: 2, product_name: '너구리', ingredient: '성분1, 성분2, 성분3', product_img: 'neoguri.png' },
  { id: 3, product_name: '메로나', ingredient: '성분1, 성분2, 성분3', product_img: 'melon.png' },
  { id: 4, product_name: '홈런볼', ingredient: '성분1, 성분2, 성분3', product_img: 'homerun.png' },
];

function List() {
  return (
    <div className="list-container">
      {defaultData.map(item => (
        <ListItem key={item.id} image={item.product_img} name={item.product_name} ingredients={item.ingredient} />
      ))}
    </div>
  );
}

export default List;
