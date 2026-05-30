SELECT 
    id as enrollment_id, 
    student_id, 
    course_id, 
    date_ as enrollment_date, 
    status as enrollment_status
FROM {{ source('raw', 'enrollments') }}