
SELECT t.* FROM tickets t
where t.passenger_name between 'P' and 'S'
order by t.passenger_name;