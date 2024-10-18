-- create table 'users' with 3 attributes
-- id(int) email(string name(string)
-- Script should not fail if file already exits
-- Yours scirpt can be executed on any database
CREATE TABLE IF NOT EXISTS users (
	id INT AUTO_INCREMENT PRIMARY KEY,
	email VARCHAR(255) NOT NULL UNIQUE,
	name VARCHAR(255)
);
