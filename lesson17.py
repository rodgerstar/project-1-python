# dates
from datetime import date, timedelta

today = date.today()
print(today)

formatted_date = today.strftime("%a %d/%m/%Y")
print(formatted_date)

after_thirty_days = today + timedelta(hours=30)
print(after_thirty_days)

