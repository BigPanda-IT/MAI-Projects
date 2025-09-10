select * from public.third_year_students lt inner join public.professors using (id)
where gruppa + graduation_year < 8;