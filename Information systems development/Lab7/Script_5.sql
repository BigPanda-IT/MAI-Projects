
SELECT t.* FROM tickets t
where t.passenger_name like 'MA%' and t.book_ref like 'B92%'
order by t.passenger_name;
--Создаем запрос который ищет людей имя который начинается на MA и book_ref начинается на B92--