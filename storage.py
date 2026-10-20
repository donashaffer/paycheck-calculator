import os
import csv

filename = "paycheck_history.csv"

def save_history(day_records):
    file_exists = os.path.isfile(filename)
    with open(filename, mode="a", newline="") as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(["Date", "Clock In", "Clock Out", "Lunch Start", "Lunch End", "Hours Worked", "Pay"])        
        writer.writerows(day_records)