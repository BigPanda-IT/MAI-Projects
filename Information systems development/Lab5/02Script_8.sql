select lt.key1,
lt.name_,
lt.key2,
rt.key3,
rt.city
from public.left_table lt
inner join public.right_table rt on lt.key2 >= rt.key3
where lt.key1 = 1717;