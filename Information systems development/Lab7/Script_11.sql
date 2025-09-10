select * from ticket_flights tf 
where tf.flight_id in
	(SELECT f.flight_id 
	FROM flights f
	where f.actual_departure is not null 
	and f.actual_departure between '2017-07-20' and '2017-07-25'
	and f.actual_arrival - f.actual_departure > '09:00:00');