CREATE DATABASE IF NOT EXISTS customers;

USE customers;

CREATE TABLE IF NOT EXISTS customers(
  id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(255) DEFAULT "no-name"
);

INSERT INTO customers VALUES
(NULL, "customer 1"),
(NULL, "customer 2"),
(NULL, "customer 3"),
(NULL, "customer 4"),
(NULL, "customer 5");
