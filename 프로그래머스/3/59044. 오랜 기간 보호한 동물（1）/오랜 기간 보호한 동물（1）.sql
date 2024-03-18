-- 코드를 입력하세요
select ai.NAME, ai.DATETIME
from ANIMAL_INS ai left join ANIMAL_OUTS ao
on ai.ANIMAL_ID = ao.ANIMAL_ID
where ao.ANIMAL_ID is NULL
order by DATETIME
limit 3