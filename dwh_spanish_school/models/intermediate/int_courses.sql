SELECT 
    course_id, 
    "level",    
    "type", 
    duration, 
    price, 
    datefrom, 
    dateto
FROM {{ ref('stg_courses') }}
WHERE 
    price <> 0.00 AND dateto > datefrom