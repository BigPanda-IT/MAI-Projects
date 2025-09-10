select tt.t1 x, tt.t2 y
from public.top_table tt
intersect
select bt.b1, bt.b2
from public.bottom_table bt;