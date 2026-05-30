import os
import psycopg

from dotenv import load_dotenv
from model import CourseDates, EnrollmentCourseDates

load_dotenv()

conn = psycopg.connect(
    host=os.getenv('PG_HOST'),
    dbname=os.getenv('PG_DB'),
    user=os.getenv('PG_USER'),
    password=os.getenv('PG_PWD')
)

def get_student_ids() -> list:
    with conn.cursor() as cur:
        cur.execute("select id from students")
        return [row[0] for row in cur.fetchall()]
    
def get_course_ids() -> list:
    with conn.cursor() as cur:
        cur.execute("select id from courses")
        return [row[0] for row in cur.fetchall()]
    
def get_enrollment_ids() -> list:
    with conn.cursor() as cur:
        cur.execute("select id from enrollments")
        return [row[0] for row in cur.fetchall()]
    
def get_course_dates(course_id: int):
    with conn.cursor() as cur:
        cur.execute("select id, datefrom, dateto from courses where id = %s", (course_id,))
        return CourseDates(*cur.fetchone())
    
def get_course_dates_by_enrollment_id(enrollment_id: int):
    with conn.cursor() as cur:
        cur.execute(
            """
                select 
                    c.id as course_id, 
                    e.id as enrollment_id,
                    e.date_ as enrollment_date,
                    e.status,
                    c.datefrom, 
                    c.dateto 
                from enrollments e
                join courses c on e.course_id = c.id
                where e.id = %s
            """, (enrollment_id,))
        return EnrollmentCourseDates(*cur.fetchone())

def insert_students(students: list):
    with conn.cursor() as cur:
        cur.executemany("""
            INSERT INTO students (name, email, regdate, country)
            VALUES (%(name)s, %(email)s, %(regdate)s, %(country)s)
        """, students)

def insert_courses(courses: list):
    with conn.cursor() as cur:
        cur.executemany("""
            INSERT INTO courses (level, type, duration, price, datefrom, dateto)
            VALUES (%(level)s, %(type)s, %(duration)s, %(price)s, %(datefrom)s, %(dateto)s)
        """, courses)

def insert_enrollments(enrollments: list):
    with conn.cursor() as cur:
        cur.executemany("""
            INSERT INTO enrollments (student_id, course_id, date_, status)
            VALUES (%(student_id)s, %(course_id)s, %(date_)s, %(status)s)
        """, enrollments)

def insert_lessons(lessons: list):
    with conn.cursor() as cur:
        cur.executemany("""
            INSERT INTO lessons (enrollment_id, date_, status, rating)
            VALUES (%(enrollment_id)s, %(date_)s, %(status)s, %(rating)s)
        """, lessons)

def insert_subscriptions(subscriptions: list):
    with conn.cursor() as cur:
        cur.executemany("""
            INSERT INTO subscriptions (student_id, plan, datefrom, dateto, status)
            VALUES (%(student_id)s, %(plan)s, %(datefrom)s, %(dateto)s, %(status)s)
        """, subscriptions)
        