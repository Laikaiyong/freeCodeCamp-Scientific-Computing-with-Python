def add_time(time, duration, day=None):
    days = ('Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday')
    midday = ('PM', 'AM')
    final_day = ""
    final_recent = ""

    time_splitted, time_period = time.split(" ")
    time_hour, time_minute = map(int, time_splitted.split(":"))
    added_hour, added_minute = map(int, duration.split(":"))
    
    extra_hours, final_minute = divmod(time_minute + added_minute, 60)
    cycle, final_hour = divmod(time_hour + extra_hours + added_hour, 12)

    period_index = abs(midday.index(time_period) - (cycle % 2))
    passed_days = (period_index + cycle) // 2

    if final_hour == 0:
        final_hour = 12
    
    if day:
        final_day = f', {days[(days.index(day.capitalize()) + passed_days) % 7]}'

    if passed_days == 1:
        final_recent = ' (next day)'
    elif passed_days > 1:
        final_recent = f' ({passed_days} days later)'


    final_time = '{}:{} {}{}{}'.format(
        final_hour,
        str(final_minute).zfill(2),
        midday[period_index],
        final_day,
        final_recent
    )
    return final_time

print(add_time("3:00 PM", "3:10"))
# Returns: 6:10 PM

print(add_time("11:30 AM", "2:32", "Monday"))
# Returns: 2:02 PM, Monday

print(add_time("11:43 AM", "00:20"))
# Returns: 12:03 PM

print(add_time("10:10 PM", "3:30"))
# Returns: 1:40 AM (next day)

print(add_time("11:43 PM", "24:20", "tueSday"))
# Returns: 12:03 AM, Thursday (2 days later)

print(add_time("6:30 PM", "205:12"))
# Returns: 7:42 AM (9 days later)