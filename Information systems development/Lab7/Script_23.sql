SELECT passenger_name, MAX(amount) AS max_amount
FROM st02demo.ticket_flights tf
JOIN st02demo.tickets t ON tf.ticket_no = t.ticket_no
GROUP BY passenger_name;