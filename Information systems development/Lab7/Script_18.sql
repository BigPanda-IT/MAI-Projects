SELECT *,f.actual_arrival - f.actual_departure dl FROM flights f
where f.actual_departure is not null 
and f.actual_departure not between '2017-07-19' and '2017-07-20'
and f.actual_arrival - f.actual_departure > '09:00:00';