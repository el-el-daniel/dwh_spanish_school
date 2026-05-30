SELECT 
    lesson_id, 
    enrollment_id, 
    lesson_date, 
    lesson_status, 
    rating,
    EXTRACT(MINUTE FROM lesson_date) NOT IN (0, 30) AS is_irregular_time
FROM {{ ref('stg_lessons') }}
WHERE 
    (lesson_status  = 'skipped' AND rating is null) OR 
    (lesson_status  <> 'skipped' AND rating is not null)