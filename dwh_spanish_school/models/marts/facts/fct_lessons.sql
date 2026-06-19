select 
    l.lesson_id, 
    l.enrollment_id, 
    e.student_id, 
    e.course_id, 
    l.lesson_date, 
    l.lesson_status, 
    l.rating,
    l.is_irregular_time,
    e.enrollment_date, 
    e.enrollment_status,
    c.datefrom as course_datefrom,
    c.dateto as course_dateto,
    c.price,
    c."level",    
    c."type"
from {{ ref('int_lessons') }} l
join {{ ref('int_enrollments') }} e using (enrollment_id)
join {{ ref('int_courses') }} c using (course_id)