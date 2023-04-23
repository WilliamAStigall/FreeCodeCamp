def add_time(start, duration, day=None):
    # Parse the start time
    start_time, period = start.split()
    start_hour, start_minute = map(int, start_time.split(':'))

    # Parse the duration
    duration_hour, duration_minute = map(int, duration.split(':'))

    # Calculate the end minute
    end_minute = (start_minute + duration_minute) % 60

    # Calculate the end hour
    end_hour = start_hour + duration_hour + (start_minute + duration_minute) // 60

    # Adjust the end hour based on the period
    if period == 'PM':
        end_hour += 12

    # Calculate the number of days that have passed
    days_passed = end_hour // 24

    # Calculate the final hour
    final_hour = end_hour % 24

    # Determine the final period
    if final_hour < 12:
        final_period = 'AM'
        if final_hour == 0:
            final_hour = 12
    else:
        final_period = 'PM'
        if final_hour > 12:
            final_hour -= 12

    # Construct the final time string
    final_time = '{:d}:{:02d} {}'.format(final_hour, end_minute, final_period)

    # Add the number of days passed to the output string

    # Determine the final day of the week if specified
    if day is not None:
        day = day.capitalize()
        weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        day_index = weekdays.index(day)
        final_day_index = (day_index + days_passed) % 7
        final_day = weekdays[final_day_index]
        final_time += ', {}'.format(final_day)
    if days_passed == 1:
        final_time += ' (next day)'
    elif days_passed > 1:
        final_time += ' ({} days later)'.format(days_passed)

    return final_time
