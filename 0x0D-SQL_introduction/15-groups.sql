-- Count the occurrences of each score value in the 'second_table'
-- table and order them by count in descending order
SELECT score, COUNT(score) AS `number`
FROM second_table
GROUP BY score
ORDER BY number DESC;
