from db import *
from generators import *
from random import sample

if __name__ == '__main__':
    with conn.transaction():
        print("Generating students")
        students = [gen_students() for _ in range(1847)]
        insert_students(students)

        print("Generating courses")
        courses = [gen_courses() for _ in range(143)]
        insert_courses(courses)

        print("Generating enrollments")
        student_ids = get_student_ids()
        course_ids = get_course_ids()
        enrollments = [e for e in [gen_enrollments(student_ids, course_ids) for _ in range(7634)] if e is not None]
        enrollments_dupl = sample(enrollments, 23)
        insert_enrollments(enrollments)
        insert_enrollments(enrollments_dupl)

        print("Generating lessons")
        enrollment_ids = get_enrollment_ids()
        lessons = [l for l in [gen_lessons(enrollment_ids) for _ in range(38291)] if l is not None]
        insert_lessons(lessons)

        print("Generating subscriptions")
        subscriptions = [gen_subscriptions(student_ids) for _ in range(2943)]
        insert_subscriptions(subscriptions)
