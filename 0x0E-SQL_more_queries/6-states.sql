-- Create a database named 'hbtn_0d_usa' if it doesn't exist
-- Create a table 'states' in the newly created database
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

USE hbtn_0d_usa;

CREATE TABLE IF NOT EXISTS states (
    id INT UNIQUE NOT NULL AUTO_INCREMENT,
    name VARCHAR(256) NOT NULL, PRIMARY KEY(id)
);
