SELECT avg( f.actual_arrival- f.actual_departure), 
f.departure_airport, f.arrival_airport 
FROM flights f
where f.actual_arrival is not null 
group by f.departure_airport, f.arrival_airport;