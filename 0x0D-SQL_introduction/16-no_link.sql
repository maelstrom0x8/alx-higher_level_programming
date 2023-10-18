-- Select the 'score' and 'name' columns from the 'second_table'
-- table and order the results by 'score' in descending order
SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
