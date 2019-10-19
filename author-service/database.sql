CREATE DATABASE IF NOT EXISTS authors;

USE authors;

CREATE TABLE IF NOT EXISTS authors(
  id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(255) DEFAULT "no-name",
  city VARCHAR(255) NOT NULL,
  state VARCHAR(255) NOT NULL
);

INSERT INTO authors VALUES
(NULL, "name 1", "city 1", "state 1"),
(NULL, "name 2", "city 2", "state 2"),
(NULL, "name 3", "city 3", "state 3"),
(NULL, "name 4", "city 4", "state 4"),
(NULL, "name 5", "city 5", "state 5"),
(NULL, "name 6", "city 6", "state 6"),
(NULL, "name 7", "city 7", "state 7"),
(NULL, "name 8", "city 8", "state 8"),
(NULL, "name 9", "city 9", "state 9");
