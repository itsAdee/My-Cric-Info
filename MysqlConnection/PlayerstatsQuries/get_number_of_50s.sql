select count(fk_Match_Id) as "50s" from batterstatsininning
where fk_batter_id in ( select player_id from player where First_name like '%Muhammad%' or Last_Name like '%Rizwan%' )
and fk_match_id in ( select Match_id from matchfixture where match_type = 'T20' )
and runs_scored > 50
group by fk_batter_id