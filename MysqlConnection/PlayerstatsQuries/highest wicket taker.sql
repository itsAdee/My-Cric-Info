select sum(runs_scored) as total_runs , fk_batter_id from batterstatsininning
where fk_batter_id in ( select player_id  from player where Country = "Pakistan")
and fk_Match_Id in (select Match_id from matchfixture where match_type = 'T20')
group by fk_batter_id