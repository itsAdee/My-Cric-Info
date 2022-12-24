use cricinfosystem2;
select sum(extra_runs) + sum(scored_runs) as Totalscore,Match_id,inning
from balls 
group by Match_id,inning
