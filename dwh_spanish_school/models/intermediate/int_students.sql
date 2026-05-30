SELECT 
    student_id, 
    INITCAP(LOWER(TRIM("name"))) AS "name", 
    email, 
    registration_date, 
    country
FROM {{ ref('stg_students') }}
WHERE email ~ '^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'