-- Products 테이블
CREATE TABLE products (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    brand VARCHAR(255),
    category VARCHAR(100),
    ingredients TEXT,
    nutritional_info TEXT,
    barcode VARCHAR(50) UNIQUE
);

-- Ratings 테이블
CREATE TABLE ratings (
    id SERIAL PRIMARY KEY,
    product_id INTEGER REFERENCES products(id) ON DELETE CASCADE,
    score INTEGER CHECK (score >= 0 AND score <= 100),
    criteria VARCHAR(255)
);

-- Users 테이블
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL
);

-- Reviews 테이블
CREATE TABLE reviews (
    id SERIAL PRIMARY KEY,
    product_id INTEGER REFERENCES products(id) ON DELETE CASCADE,
    user_id INTEGER REFERENCES users(id) ON DELETE CASCADE,
    review TEXT,
    rating INTEGER CHECK (rating >= 0 AND rating <= 100)
);