select count(*) as wickets,fk_match_id,InningNumber
from wicketstatsinnings
group by fk_Match_id,InningNumber