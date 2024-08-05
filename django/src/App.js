import React from 'react';
import Header from './components/Header';
import ListItem from './pages/ListItem';
import Footer from './components/Footer';

function App() {
  return (
    <div>
      <Header />
      <div className="list-container">
        <ListItem image="shinramen.png" name="신라면" ingredients="성분1, 성분2, 성분3" />
        <ListItem image="neoguri.png" name="너구리" ingredients="성분1, 성분2, 성분3" />
        <ListItem image="melon.png" name="메로나" ingredients="성분1, 성분2, 성분3" />
        <ListItem image="homerun.png" name="홈런볼" ingredients="성분1, 성분2, 성분3" />
      </div>
      <button className="load-more">Load more</button>
      <Footer />
    </div>
  );
}

export default App;
