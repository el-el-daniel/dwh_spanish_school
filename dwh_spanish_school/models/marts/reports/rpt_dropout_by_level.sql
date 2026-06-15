with dropped_levels as (
    select c.level, count(*) as cnt
    from {{ ref('fct_lessons') }} l
    join {{ ref('dim_courses') }} c using (course_id)
    where enrollment_status = 'dropped'
    group by c.level
)
select level, cnt / sum(cnt) over() * 100 as percentage
from dropped_levels