from datetime import datetime

time_format = "%H%M"
hourly_rate = float(input("Enter hourly rate: "))
num_days = int(input("How many days do you want to enter? "))

total_pay = 0
total_hours_all_days = 0

for day in range(1, num_days + 1):
    print(f"\n--- Day {day} ---")
    clock_in = input("Enter clock-in time (Military time e.g., 0900 for 9:00 AM): ")
    clock_out = input("Enter clock-out time (Military time e.g., 1700 for 5:00 PM): ")
    lunch_start = input("Enter lunch start time (Military time e.g., 1200 for 12:00 PM): ")
    lunch_end = input("Enter lunch end time (Military time e.g., 1300 for 1:00 PM): ")

    in_time = datetime.strptime(clock_in, time_format)
    out_time = datetime.strptime(clock_out, time_format)
    lunch_start_time = datetime.strptime(lunch_start, time_format)
    lunch_end_time = datetime.strptime(lunch_end, time_format)

    total_worked = out_time - in_time
    total_hours = total_worked.total_seconds() / 3600

    lunch_duration = lunch_end_time - lunch_start_time
    lunch_hours = lunch_duration.total_seconds() / 3600

    hours_worked = total_hours - lunch_hours  
    day_pay = hours_worked * hourly_rate

    print(f"Hours worked: {hours_worked:.2f}")
    print(f"Pay for this day: ${day_pay:.2f}")

    total_hours_all_days += hours_worked
    total_pay += day_pay


print(f"\n--- Summary ---")
print(f"Total hours worked: {total_hours_all_days:.2f}")
print(f"Total pay: ${total_pay:.2f}")