select sum(runs_scored)/sum(ballfaced) * 100 as strike_rate
from batterstatsininning
where fk_batter_id in ( select player_id from player where First_name like '%virat%' or Last_Name like '%kohli%' )
and fk_match_id in ( select Match_id from matchfixture where match_type = 'T20' )
group by fk_batter_id