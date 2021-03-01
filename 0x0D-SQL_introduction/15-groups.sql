--counting number of times values have been repeated.
SELECT score FROM second_table ORDER BY score DESC HAVING COUNT(score) AS number ORDER BY score;
