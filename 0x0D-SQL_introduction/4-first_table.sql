-- Create a table named 'first_table' if it doesn't exist
-- with columns 'id' of type INT and 'name' of type VARCHAR(256)
CREATE TABLE IF NOT EXISTS first_table (
    id INT DEFAULT NULL,
    name VARCHAR(256)
);
