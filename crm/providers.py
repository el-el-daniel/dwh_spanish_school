from datetime import date
from dateutil.relativedelta import relativedelta
from faker.providers import DynamicProvider

starts = []
current = date(2022, 9, 1)
while current <= date.today():
    starts.append(current)
    current += relativedelta(months=3)

language_level_provider = DynamicProvider(
    provider_name="language_level",
    elements=["A1", "A2", "B1", "B2", "C1", "C2"]
)
course_type_provider = DynamicProvider(
    provider_name="course_type",
    elements=["group", "individual", "intensive"]
)
duration_provider = DynamicProvider(
    provider_name="duration",
    elements=[4, 8, 12, 16]
)
course_starts_provider = DynamicProvider(
    provider_name="course_start",
    elements=starts
)
