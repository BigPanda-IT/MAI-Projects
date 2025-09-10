-- bookings.flights_v исходный текст

CREATE OR REPLACE VIEW bookings.flights_v
AS SELECT f.flight_id,
    f.flight_no,
    f.scheduled_departure,
    timezone(dep.timezone, f.scheduled_departure) AS scheduled_departure_local,
    f.scheduled_arrival,
    timezone(arr.timezone, f.scheduled_arrival) AS scheduled_arrival_local,
    f.scheduled_arrival - f.scheduled_departure AS scheduled_duration,
    f.departure_airport,
    dep.airport_name AS departure_airport_name,
    dep.city AS departure_city,
    f.arrival_airport,
    arr.airport_name AS arrival_airport_name,
    arr.city AS arrival_city,
    f.status,
    f.aircraft_code,
    f.actual_departure,
    timezone(dep.timezone, f.actual_departure) AS actual_departure_local,
    f.actual_arrival,
    timezone(arr.timezone, f.actual_arrival) AS actual_arrival_local,
    f.actual_arrival - f.actual_departure AS actual_duration
   FROM flights f,
    airports dep,
    airports arr
  WHERE f.departure_airport = dep.airport_code AND f.arrival_airport = arr.airport_code;