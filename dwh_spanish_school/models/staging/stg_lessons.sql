SELECT 
    id as lesson_id, 
    enrollment_id, 
    date_ as lesson_date, 
    status as lesson_status, 
    rating
FROM {{ source('raw', 'lessons') }}
WHERE rating IS NOT NULL AND RATING <= 5 AND RATING >= 1