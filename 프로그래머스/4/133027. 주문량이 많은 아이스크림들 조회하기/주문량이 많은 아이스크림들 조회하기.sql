-- 코드를 입력하세요
select FLAVOR
from (select * from FIRST_HALF union all select * from JULY) ab
group by FLAVOR
order by sum(TOTAL_ORDER) desc
limit 3