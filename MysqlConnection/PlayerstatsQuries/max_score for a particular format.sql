select max(runs_scored) from batterstatsininning
where fk_batter_id in ( select player_id from player where First_name like '%Virat%' or Last_Name like '%Kohli%' )
and fk_match_id in ( select Match_id from matchfixture where match_type = 'T20' )
group by fk_batter_id