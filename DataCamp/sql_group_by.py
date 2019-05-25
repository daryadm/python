# A word of warning: SQL will return an error if you try to SELECT a field that
# is not in your GROUP BY clause without using it to calculate some kind of value
# about the entire group.

select release_year
from films
group by release_year
having count(*) > 200;
========================================================================

select release_year, avg(budget) as avg_budget, avg(gross) as avg_gross
from films
where release_year > 1990
group by release_year
having avg(budget) > 60000000
order by avg(gross) desc;
==========================================================================

-- select country, average budget, average gross
select country, avg(budget) as avg_budget, avg(gross) as avg_gross
-- from the films table
from films
-- group by country
group by country
-- where the country has a title count greater than 10
having count(*) > 10
-- order by country
order by country limit 5

-- limit to only show 5 results
===========================================================================
