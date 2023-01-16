select sum(runs)/sum(deliveries) * 100 as strike_rate
from bowlerstatsininning
where fk_bowler_id in ( select player_id from player where First_name like '%Shaheen%' or Last_Name like '%Afridi%' )
and fk_match_id in ( select Match_id from matchfixture where match_type = 'T20' )
group by fk_bowler_id