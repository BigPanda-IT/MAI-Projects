SELECT AVG(actual_arrival - actual_departure) AS avg_duration
FROM st02demo.flights
WHERE status = 'Arrived';