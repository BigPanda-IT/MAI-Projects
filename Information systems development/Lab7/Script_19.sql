SELECT *
FROM flights f
where f.actual_departure between '2017-01-01' and '2017-12-31'
order by f.actual_departure;