select count(*) as '3w'
from (select count(*) as '3w'
from wicketstatsinnings
where BowlerId in ( select player_id from player where First_name like '%Shaheen%' or Last_Name like '%Afridi%' )
and fk_match_id in ( select Match_id from matchfixture where match_type = 'T20' )
group by BowlerId , fk_match_id
having count(*) >= 3) as anothertable