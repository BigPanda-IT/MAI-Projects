select * from public.third_year_students lt left join public.professors using (id)
where lt.last_name like '%е%'
order by lt.gruppa;
