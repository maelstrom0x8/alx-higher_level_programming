-- Create a MySQL user named 'user_0d_1' with a password and
-- grant all privileges to them on all databases from 'localhost'
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';
