SELECT departure_airport, arrival_airport, COUNT(*) AS flights_count
FROM st02demo.flights
GROUP BY departure_airport, arrival_airport
HAVING COUNT(*) > 3
ORDER BY departure_airport, arrival_airport;