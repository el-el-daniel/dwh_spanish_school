SELECT 
    id as lesson_id, 
    enrollment_id, 
    date_ as lesson_date, 
    status as lesson_status, 
    rating
FROM {{ source('raw', 'lessons') }}