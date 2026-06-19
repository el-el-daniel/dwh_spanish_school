select 
    course_id, 
    "level",    
    "type", 
    duration, 
    price, 
    datefrom, 
    dateto
from {{ ref('int_courses') }}