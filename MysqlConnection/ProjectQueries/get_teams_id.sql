Select *
from matchfixture join series using(series_id)
where fk_team_1_id in (select team_id from team where team_name = "Zimbabwe" or team_name = "India")
or fk_team_2_id in (select team_id from team where team_name = "Zimbabwe" or team_name = "India")