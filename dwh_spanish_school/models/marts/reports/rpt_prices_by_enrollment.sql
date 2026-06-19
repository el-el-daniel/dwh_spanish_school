select distinct 
    enrollment_id, 
    student_id, 
    course_id, 
    "level",    
    "type",
    price,
    extract(year from course_datefrom) as "year",
    extract(month from lesson_date) as "month"
from {{ ref('fct_lessons') }} l