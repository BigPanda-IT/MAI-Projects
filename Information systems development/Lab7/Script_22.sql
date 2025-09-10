SELECT flight_id, flight_no, departure_airport, arrival_airport
FROM st02demo.flights
WHERE DATE(scheduled_departure) = '2017-08-01';