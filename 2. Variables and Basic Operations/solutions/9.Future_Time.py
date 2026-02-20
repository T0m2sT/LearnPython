current_hours = 18
current_minutes = 7
carry_on_hours = 0
carry_on_days = 0

hours_sleeping = int(input("How many hours will you be sleeping? "))
minutes_sleeping = int(input("And how many minutes will you be sleeping? "))

current_minutes += minutes_sleeping
if current_minutes >= 60:
    carry_on_hours = current_minutes // 60
    current_minutes %= 60

current_hours = current_hours + hours_sleeping + carry_on_hours
if current_hours >= 24:
    carry_on_days = current_hours // 24
    current_hours %= 24

print("Wake-Up time:", str(current_hours) + ":" + str(current_minutes))

if carry_on_days != 0:
    print("Not the same day,", carry_on_days, "day(s) after you slept.")