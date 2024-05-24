-- Display count of a particular score in the database
SELECT score, COUNT(*) AS number FROM second_table
GROUP BY score
ORDER number BY DESC;
