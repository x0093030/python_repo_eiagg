# This script creates a database and a table in MySQL
# This script was grnerated with MySWL Workbench

# CREATE DATABASE prueba;

USE prueba;

CREATE TABLE usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50),
    email VARCHAR(100)
);