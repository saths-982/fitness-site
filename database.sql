USE fitness_db;
CREATE DATABASE fitness_coaching;
USE fitness_coaching;

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    age INT NOT NULL,
    gender VARCHAR(10) NOT NULL,
    goal VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL
);
INSERT INTO users (name, email, password) 
VALUES ('John Doe', 'john@example.com', 'securepassword');
SELECT * FROM users;

