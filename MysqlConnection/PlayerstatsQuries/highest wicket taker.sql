-- this query is a part of python script
(select count(*)  as wickets , BowlerId from wicketstatsinnings
where BowlerId in ( select player_id  from player where Country = "Pakistan")
and fk_Match_Id in (select Match_id from matchfixture where match_type = 'T20')
group by BowlerId) 
