CREATE DATABASE IF NOT EXISTS books;

USE books;

CREATE TABLE IF NOT EXISTS books(
  id INT AUTO_INCREMENT PRIMARY KEY,
  title VARCHAR(255) DEFAULT "no-name",
  price INT NOT NULL,
  author_id INT NOT NULL
);

INSERT INTO books VALUES
(NULL, "title 1", 10000, 1),
(NULL, "title 2", 15000, 3),
(NULL, "title 3", 55000, 7),
(NULL, "title 4", 20000, 2),
(NULL, "title 5", 25000, 4);
