select count(*) as losses from matchfixture
where (fk_team_1_id in ( select team_id from team  where  team_name = 'Pakistan')
or fk_team_2_id in (select team_id from team where team_name = 'Pakistan')) and
Matchwinner = 0
and match_type = 'T20'