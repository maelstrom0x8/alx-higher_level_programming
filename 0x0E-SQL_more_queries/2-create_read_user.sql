-- Create a MySQL database named 'hbtn_0d_2' if it doesn't exist
-- Create a MySQL user named 'user_0d_2' without a password
-- Grant the SELECT privilege on all tables in the 'hbtn_0d_2' database to 'user_0d_2' from 'localhost'
CREATE DATABASE IF NOT EXISTS `hbtn_0d_2`;
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost';
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';
