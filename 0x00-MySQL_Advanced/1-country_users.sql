-- creates a table users following these attributes
-- id email name country
-- if it exists script should not fail
-- scipt can be executed in any database
-- key concept: ENUM('value1', 'value2' ...) 
-- enforces a strict list of possible options
CREATE TABLE IF NOT EXISTS users (
	id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
	email VARCHAR(255) NOT NULL UNIQUE,
	name VARCHAR(255),
	country ENUM('US', 'CO', 'TN') DEFAULT 'US' NOT NULL
);
