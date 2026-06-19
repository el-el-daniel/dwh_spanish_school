select distinct 
    enrollment_id, 
    student_id, 
    course_id, 
    "level",    
    "type",
    price,
    "year",
    "month"
from {{ ref('fct_lessons') }} l