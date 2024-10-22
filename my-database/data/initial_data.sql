-- 초기 데이터 추가

-- Products 테이블 데이터
INSERT INTO products (name, brand, category, ingredients, nutritional_info, barcode)
VALUES 
('Apple', 'Organic Farm', 'Fruits', 'Apples', 'Calories: 52', '1234567890123'),
('Banana', 'Tropical Farms', 'Fruits', 'Bananas', 'Calories: 89', '1234567890124');

-- Users 테이블 데이터
INSERT INTO users (username, email, password)
VALUES 
('john_doe', 'john@example.com', 'securepassword'),
('jane_doe', 'jane@example.com', 'securepassword');