from datetime import datetime
from datetime import timedelta


def display_current_datetime():
    current_date = datetime.now()
    formatted = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(formatted)


display_current_datetime()
