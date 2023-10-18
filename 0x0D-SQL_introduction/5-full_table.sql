-- Retrieve information about columns in the 'first_table' table
-- within the 'hbtn_0c_0' database from the information_schema.COLUMNS table
SELECT *
FROM information_schema.COLUMNS
WHERE TABLE_SCHEMA = 'hbtn_0c_0' AND TABLE_NAME = 'first_table';
