select count(*) from bowlerstatsininning
join wicketstatsinnings on bowlerstatsininning.fk_Match_Id = wicketstatsinnings.fk_match_id
where BowlerId = 784379 and fk_bowler_id = 784379
and wicketstatsinnings.InningNumber = 1