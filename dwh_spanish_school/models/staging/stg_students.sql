SELECT 
    id as student_id, 
    "name", 
    email, 
    regdate as registration_date, 
    country
FROM {{ source('raw', 'students') }}