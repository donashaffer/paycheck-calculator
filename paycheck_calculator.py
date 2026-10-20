import streamlit as st
from datetime import datetime
from utils import parse_time_flexible
import csv
import os
from storage import save_history

st.title("Paycheck Calculator")

filename = "paycheck_history.csv"
0
hourly_rate = st.number_input("Enter hourly rate: ")
num_days = int(st.number_input("How many days do you want to enter? ", min_value=1, value=1, step=1))

total_pay = 0
total_hours_all_days = 0
day_records = []

for day in range(1, num_days + 1):
    st.subheader(f"Day {day}")
    work_date = st.date_input(f"Date for Day {day}", key=f"date{day}")
    clock_in = st.text_input(f"Enter clock-in time (e.g., 0900) - Day {day}: ", key=f"in{day}")
    clock_out = st.text_input(f"Enter clock-out time (e.g., 1700) - Day {day}: ", key=f"out{day}")
    lunch_start = st.text_input(f"Enter lunch start time (e.g., 1200) - Day {day}: ", key=f"lunch_start{day}")
    lunch_end = st.text_input(f"Enter lunch end time (e.g., 1300) - Day {day}: ", key=f"lunch_end{day}")

if st.button("Calculate"):
    error_found = False

    for day in range(1, num_days + 1):
        work_date = st.session_state[f"date{day}"]

        try:
            in_time = parse_time_flexible(st.session_state[f"in{day}"])
            out_time = parse_time_flexible(st.session_state[f"out{day}"])
            lunch_start_time = parse_time_flexible(st.session_state[f"lunch_start{day}"])
            lunch_end_time = parse_time_flexible(st.session_state[f"lunch_end{day}"])
        except ValueError:
            st.error(f"Day {day}: Please enter times in 4-digit military format, like 0900 or 1730.")
            error_found = True
            continue

        total_hours = (out_time - in_time).total_seconds() / 3600
        lunch_hours = (lunch_end_time - lunch_start_time).total_seconds() / 3600
        hours_worked = total_hours - lunch_hours

        if hours_worked < 0:
            st.error(f"Day {day}: Clock-out time is before clock-in time. Please double check.")
            error_found = True
            continue

        day_pay = hours_worked * hourly_rate

        st.write(f"{work_date.strftime('%A, %B %d, %Y')}: Hours worked: {hours_worked:.2f} hrs - ${day_pay:.2f}")

        total_hours_all_days += hours_worked
        total_pay += day_pay

        day_records.append([
            work_date.strftime("%Y-%m-%d"),
            st.session_state[f"in{day}"],
            st.session_state[f"out{day}"],
            st.session_state[f"lunch_start{day}"],
            st.session_state[f"lunch_end{day}"],
            f"{hours_worked:.2f}",
            f"{day_pay:.2f}"
        ])

    if not error_found:
        st.subheader("Summary")
        st.write(f"Total hours worked: {total_hours_all_days:.2f}")
        st.write(f"Total pay: ${total_pay:.2f}")

        save_history(day_records)

        st.write(f"Saved to {filename}")