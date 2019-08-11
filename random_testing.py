import datetime as dt
from datetime import datetime

start_date = dt.date(2019, 2, 4)
print(start_date)


current_date = dt.date.today()
print (current_date)
time = current_date - start_date
print (int(time.days))
