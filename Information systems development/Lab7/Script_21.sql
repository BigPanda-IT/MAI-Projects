SELECT t1.passenger_name, t1.ticket_no, tf.amount
FROM st02demo.tickets t1
JOIN (
SELECT ticket_no, MAX(amount) AS max_amount
FROM st02demo.ticket_flights
GROUP BY ticket_no
) tf_max ON t1.ticket_no = tf_max.ticket_no
JOIN st02demo.ticket_flights tf ON t1.ticket_no = tf.ticket_no
WHERE tf.amount = tf_max.max_amount;