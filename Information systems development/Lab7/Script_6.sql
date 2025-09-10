SELECT f.actual_departure, f.actual_arrival FROM flights f
where f.actual_departure is not null and f.actual_arrival is not null;