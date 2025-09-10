SELECT passenger_id, SUM(amount) as total_amount
FROM st02demo.vflights_tickets
GROUP BY passenger_id;