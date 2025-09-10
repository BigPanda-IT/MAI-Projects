
SELECT f.* FROM flights f
Where NOT f.departure_airport = 'SVO' or not f.departure_airport = 'AER';