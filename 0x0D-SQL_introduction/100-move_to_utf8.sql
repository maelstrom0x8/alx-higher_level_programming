-- Switch to the 'hbtn_0c_0' database
-- Alter the table 'first_table' to convert it to character set 'utf8mb4' with collation 'utf8mb4_unicode_ci'
USE `hbtn_0c_0`

ALTER TABLE `first_table`
CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
