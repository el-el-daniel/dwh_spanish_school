SELECT 
    e.enrollment_id, 
    e.student_id, 
    e.course_id, 
    e.enrollment_date, 
    e.enrollment_status
FROM {{ ref('stg_enrollments') }} e
JOIN {{ ref('stg_courses') }} c USING (course_id)
JOIN {{ ref('stg_students') }} s USING (student_id)
WHERE e.enrollment_date >= c.datefrom