
SELECT * FROM flights f
where f.arrival_airport ='VKO' and aircraft_code like '321' and
f.actual_arrival > ANY (
		SELECT f.actual_departure
		FROM flights f
		where f.actual_departure is not null
		and f.actual_arrival  - f.actual_departure between '00:20:00' and '00:25:00'
		);
