import streamlit as st
from datetime import datetime
import csv
import os

st.title("Paycheck Calculator")

time_format = "%H%M"
filename = "paycheck_history.csv"

hourly_rate = st.number_input("Enter hourly rate: ") 
num_days = int(st.number_input("How many days do you want to enter? "))

total_pay = 0
total_hours_all_days = 0
day_records = []

for day in range(1, num_days + 1):
    st.subheader(f"Day {day}")
    clock_in = st.text_input(f"Enter clock-in time (Military time e.g., 0900 for 9:00 AM) - Day {day}: ", key=f"in{day}")
    clock_out = st.text_input(f"Enter clock-out time (Military time e.g., 1700 for 5:00 PM) - Day {day}: ", key=f"out{day}")
    lunch_start = st.text_input(f"Enter lunch start time (Military time e.g., 1200 for 12:00 PM) - Day {day}: ", key=f"lunch_start{day}")
    lunch_end = st.text_input(f"Enter lunch end time (Military time e.g., 1300 for 1:00 PM) - Day {day}: ", key=f"lunch_end{day}")

if st.button("Calculate"):
    for day in range(1, int(num_days) + 1):
        in_time = datetime.strptime(st.session_state[f"in{day}"], time_format)
        out_time = datetime.strptime(st.session_state[f"out{day}"], time_format)
        lunch_start_time = datetime.strptime(st.session_state[f"lunch_start{day}"], time_format)
        lunch_end_time = datetime.strptime(st.session_state[f"lunch_end{day}"], time_format)

        total_hours = (out_time - in_time).total_seconds() / 3600
        lunch_hours = (lunch_end_time - lunch_start_time).total_seconds() / 3600
        hours_worked = total_hours - lunch_hours
        day_pay = hours_worked * hourly_rate

        st.write(f"Day {day}: Hours worked: {hours_worked:.2f} hrs - ${day_pay:.2f}")

        total_hours_all_days += hours_worked
        total_pay += day_pay

    st.subheader("Summary")
    st.write(f"Total hours worked: {total_hours_all_days:.2f}")
    st.write(f"Total pay: ${total_pay:.2f}")
