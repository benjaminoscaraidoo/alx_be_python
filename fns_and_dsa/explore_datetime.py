from datetime import datetime, timedelta, date



def display_current_datetime():
    current_date = datetime.now()
    formatted = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted}")


def calculate_future_date():
    add_days = int(input("Enter the number of days to add to the current date: "))
    future_date = date.today() + timedelta(days=add_days)
    print(f"Future date: {future_date}")


    
display_current_datetime()
calculate_future_date()
