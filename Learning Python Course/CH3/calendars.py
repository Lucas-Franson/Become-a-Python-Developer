import calendar

c = calendar.TextCalendar(calendar.MONDAY)
st = c.formatmonth(2021, 1, 0, 0)
print(st)

hc = calendar.HTMLCalendar(calendar.SUNDAY)
st = hc.formatmonth(2021, 1)
print(st)

for i in c.itermonthdays(2021, 8):
    print(i)

for name in calendar.month_name:
    print(name)

for name in calendar.day_name:
    print(name)


print("Teams meetings will be on: ")
for m in range(1, 13):
    cal = calendar.monthcalendar(2021, m)
    weekone=cal[0]
    weektwo=cal[1]

    if weekone[calendar.FRIDAY] != 0:
        meetday = weekone[calendar.FRIDAY]
    else:
        meetday = weektwo[calendar.FRIDAY]

    print("%10s %2d" % (calendar.month_name[m], meetday))