-- No of wins
select count(*) as wins from matchfixture
where (fk_team_1_id in ( select team_id from team  where  team_name = 'Pakistan')
or fk_team_2_id in (select team_id from team where team_name = 'Pakistan')) and
Matchwinner in ( select team_id from team where team_name = 'Pakistan')
and match_type = 'T20'