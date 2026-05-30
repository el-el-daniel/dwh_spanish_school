SELECT 
    id as course_id, 
    "level",    
    "type", 
    duration, 
    price, 
    datefrom, 
    dateto
FROM {{ source('raw', 'courses') }}