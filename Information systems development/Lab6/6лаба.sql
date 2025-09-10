drop view if exists tiket_flights_sum_v, tiket_flights_v02;
create or replace view tiket_flights_sum_v as
select tf.flight_id,
	sum(tf.amount) as sum_amount,
	count(tf.flight_id) as cnt
	from ticket_flights tf
	group by tf.flight_id;
	
select * from tiket_flights_sum_v;


create or replace view tiket_flights_v02 as
select fv.flight_id,
fv.flight_no,
fv.scheduled_departure,
fv.scheduled_arrival,
fv.scheduled_duration,
fv.departure_airport,
fv.departure_airport_name,
fv.departure_city,
fv.arrival_airport,
fv.arrival_airport_name,
fv.arrival_city,
fv.status,
fv.aircraft_code,
fv.actual_departure,
fv.actual_departure_local,
fv.actual_arrival,
fv.actual_arrival_local,
fv.actual_duration,
tfsv.sum_amount,
tfsv.cnt
from flights_v fv, tiket_flights_sum_v tfsv
where fv.flight_id = tfsv.flight_id
order by fv.flight_id;
