select count(fk_Match_Id) as total_Matches
from batterstatsininning
where fk_batter_id in ( select player_id from player where First_name like '%Babar%' or Last_Name like '%Azam%' )
and fk_match_id in ( select Match_id from matchfixture where match_type = 'T20' )
group by fk_batter_id