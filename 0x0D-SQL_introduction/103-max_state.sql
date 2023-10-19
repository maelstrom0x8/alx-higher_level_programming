-- Select the 'state' and calculate the maximum of 'value' while aliasing it as 'max_temp'
-- Group the results by 'state'
-- Order the results by 'state'
SELECT `state`, MAX(`value`) AS `max_temp`
FROM `temperatures`
GROUP BY `state`
ORDER BY `state`;
