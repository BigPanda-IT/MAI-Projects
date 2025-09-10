CREATE or replace VIEW vflights_tickets AS
SELECT f.flight_id, f.flight_no, f.scheduled_departure, f.scheduled_arrival, f.departure_airport, f.arrival_airport, f.status, f.aircraft_code, f.actual_departure, f.actual_arrival, tf.ticket_no, tf.fare_conditions, tf.amount, t.book_ref, t.passenger_id, t.passenger_name, t.contact_data
FROM st02demo.flights f
INNER JOIN st02demo.ticket_flights tf ON f.flight_id = tf.flight_id
INNER JOIN st02demo.tickets t ON tf.ticket_no = t.ticket_no;
select * from vflights_tickets;