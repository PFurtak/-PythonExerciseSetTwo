# prompt users for numbered day of the week and print corresponding day by name
week_days = ["Sunday", "Monday", "Tuesday",
             "Wednesday", "Thursday", "Friday", "Saturday"]

day = int(input('Day (0-6)? '))
print(week_days[day])

# let user know to sleep in on weekends or go to work on weekdays
if day == 0 or day == 6:
    print('Sleep in.')
else:
    print("Go to work.")
