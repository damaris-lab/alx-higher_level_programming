-- lists all the cities of California that can be found in the database hbtn_0d_usa.
SET @state_id = (SELECT id FROM states WHERE name = 'California');
SELECT cities.name
FROM cities
WHERE cities.state_id = @state_id
ORDER BY cities.id ASC;


