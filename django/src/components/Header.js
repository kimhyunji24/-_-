import React from 'react';
import { Link } from 'react-router-dom';

function Header() {
  return (
    <header className="header">
      <div className="logo">알,먹!</div>
      <nav>
        <ul>
          <li>
            <Link to="/">Home</Link>
          </li>
          <li>
            <Link to="/list">List</Link>
          </li>
          <li>Contact</li>
        </ul>
      </nav>
      <div className="user-icon">👤</div>
    </header>
  );
}

export default Header;
