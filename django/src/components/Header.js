import React from 'react';

function Header() {
  return (
    <header className="header">
      <div className="logo">알,먹!</div>
      <nav>
        <ul>
          <li>Home</li>
          <li>List</li>
          <li>About Us</li>
          <li>Contact</li>
        </ul>
      </nav>
      <div className="user-icon">👤</div>
    </header>
  );
}

export default Header;
