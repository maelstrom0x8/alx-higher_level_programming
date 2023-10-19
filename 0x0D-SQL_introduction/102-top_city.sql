-- Select the 'city' and calculate the average of 'value' while aliasing it as 'avg_temp'
-- Filter the data by 'month' being 7 or 8
-- Group the results by 'city'
-- Order the results by 'avg_temp' in descending order
-- Limit the output to the top 3 rows
SELECT `city`, AVG(`value`) AS `avg_temp`
FROM `temperatures`
WHERE `month` = 7 OR `month` = 8
GROUP BY `city`
ORDER BY `avg_temp` DESC
LIMIT 3;
