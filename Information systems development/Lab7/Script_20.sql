SELECT t.passenger_name, COUNT(tf.ticket_no) AS ticket_count
FROM st02demo.tickets t
JOIN st02demo.ticket_flights tf ON t.ticket_no = tf.ticket_no
GROUP BY t.passenger_name
HAVING COUNT(tf.ticket_no) > 1;