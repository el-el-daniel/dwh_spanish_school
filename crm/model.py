from datetime import date
from typing import NamedTuple

class CourseDates(NamedTuple):
    id: int
    datefrom: date
    dateto: date

class EnrollmentCourseDates(NamedTuple):
    course_id: int
    enrollment_id: int
    enrollment_date: date
    enrollment_status: str
    course_datefrom: date
    course_dateto: date
