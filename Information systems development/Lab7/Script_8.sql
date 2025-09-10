SELECT t.* FROM tickets t
where t.passenger_name  not between 'A' and 'Z'
order by t.passenger_name;