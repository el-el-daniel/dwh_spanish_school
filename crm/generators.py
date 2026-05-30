import random

from datetime import datetime, time, timedelta
from faker import Faker

from db import *
from providers import *

fake = Faker()

fake.add_provider(language_level_provider)
fake.add_provider(course_type_provider)
fake.add_provider(duration_provider)
fake.add_provider(course_starts_provider)

def gen_students() -> dict:
    # 3% email невалидные
    # 1% телефон вместо email
    email_prob = random.random()
    if email_prob <= 0.01:
        email = fake.phone_number()
    elif email_prob <= 0.03:
        email = fake.name().replace(' ', '')
    else:
        email = fake.email()

    # 1% имен с пробелом
    # 2% имён капсом
    name_prob = random.random()
    if name_prob <= 0.01:
        name = ' ' + fake.name()
    elif name_prob <= 0.02:
        name = fake.name().upper()
    else:
        name = fake.name()

    return {
        "name": name,
        "email": email,
        "regdate": fake.date_time_this_decade(),
        "country": fake.country()
    }

def gen_courses() -> dict:
    course_type = fake.course_type()
    duration_weeks = fake.duration()

    prices = {
        'group': [49.99, 79.99, 99.99],
        'individual': [149.99, 199.99, 299.99],
        'intensive': [99.99, 149.99],
    }

    # 1% нулевых цен
    price_prob = random.random()
    if price_prob <= 0.01:
        price = 0.00
    else:
        price = random.choice(prices[course_type])

    datefrom = fake.course_start()

    dateto_prob = random.random()
    if dateto_prob <= 0.005:
        dateto = fake.date_between(
            start_date=datefrom - timedelta(weeks=random.randint(1, 7)),
            end_date=datefrom
    )
    else:
        dateto = datefrom + timedelta(weeks=duration_weeks)

    return {
        "level": fake.language_level(),
        "type": course_type,
        "duration": duration_weeks,
        "price": price,
        "datefrom": datefrom,
        "dateto": dateto
    }
            
def gen_enrollments(student_ids: list, course_ids: list):
    student_id = random.choice(student_ids)
    course_id = random.choice(course_ids)

    course = get_course_dates(course_id)

    end_date = min(course.dateto, date.today())
    if course.datefrom >= end_date:
        return None

    date_prob = random.random()
    if date_prob <= 0.01:
        enrollment_date = fake.date_time_between(
            start_date=course.datefrom - timedelta(weeks=random.randint(1, 7)),
            end_date=course.datefrom
        )
    else:
        enrollment_date = fake.date_time_between(
            start_date=course.datefrom,
            end_date=end_date
        )

    if course.dateto < date.today():
        status = random.choices(['completed', 'dropped'], weights=[70, 30])[0]
    else:
        status = random.choices(['active', 'paused'], weights=[85, 15])[0]

    return {
        "student_id": student_id, 
        "course_id": course_id,
        "date_": enrollment_date,
        "status": status
    }

def gen_lessons(enrollment_ids: list):
    enrollment_id = random.choice(enrollment_ids)
    course = get_course_dates_by_enrollment_id(enrollment_id)

    end_date = min(course.course_dateto, date.today())
    if course.enrollment_date.date() >= end_date:
        return None

    lesson_times = [9, 10, 11, 14, 15, 16, 17, 18, 19, 20]

    lesson_date = fake.date_between(
        start_date=course.enrollment_date,
        end_date=end_date
    )

    hour = random.choice(lesson_times)

    if random.random() < 0.05:
        minute = random.randint(1, 59)
    else:
        minute = random.choice([0, 30])

    lesson_datetime = datetime.combine(lesson_date, time(hour, minute))
    
    if course.enrollment_status == 'dropped':
        status = random.choices(['completed', 'skipped'], weights=[30, 70])[0]
    else:
        status = random.choices(['completed', 'skipped'], weights=[85, 15])[0]

    if status == 'skipped':
        rating = None
    else:
        rating_prob = random.random()
        if rating_prob <= 0.01:
            rating = None
        elif rating_prob <= 0.03:
            rating = random.choice([0, 6])
        else:
            rating = random.choices(
                [1, 2, 3, 4, 5],
                weights=[5, 10, 20, 40, 25]
            )[0]

    return {
        "enrollment_id": enrollment_id, 
        "date_": lesson_datetime,
        "status": status,
        "rating": rating
    }

def gen_subscriptions(student_ids: list) -> dict:
    student_id = random.choice(student_ids)
    
    plan = random.choices(
        ['basic', 'standard', 'premium'],
        weights=[50, 30, 20]
    )[0]
    
    datefrom = fake.date_between(start_date='-2y', end_date='today')
    
    duration_weeks = random.choice([4, 12, 24, 52])
    date_prob = random.random()
    if date_prob <= 0.01:
        dateto = datefrom - timedelta(weeks=random.randint(1, 7))
    else:
        dateto = datefrom + timedelta(weeks=duration_weeks)
    
    if dateto < date.today():
        status = random.choices(['expired', 'cancelled'], weights=[70, 30])[0]
    else:
        status = random.choices(['active', 'paused'], weights=[85, 15])[0]
    
    return {
        "student_id": student_id,
        "plan": plan,
        "datefrom": datefrom,
        "dateto": dateto,
        "status": status
    }
