import calendar
import os
print(os.getpid())
calendar_ins = calendar.Calendar(2)

week_days = calendar_ins.monthdatescalendar(2022, 2)
print(calendar.monthrange(2022, 10))
