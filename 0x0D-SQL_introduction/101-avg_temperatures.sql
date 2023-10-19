-- Select the 'city' and calculate the average of 'value' while aliasing it as 'avg_temp'
-- Group the results by 'city'
-- Order the results by 'avg_temp' in descending order
SELECT `city`, AVG(`value`) AS `avg_temp`
FROM `temperatures`
GROUP BY `city`
ORDER BY `avg_temp` DESC;
