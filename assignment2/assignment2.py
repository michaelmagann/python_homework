import csv
import traceback

#Task 2 

def read_employees():
    employees_dict = {}
    rows = []

    try:
        with open("../csv/employees.csv", newline="") as csvfile:
            reader = csv.reader(csvfile)

            for i, row in enumerate(reader):
                if i == 0:
                    employees_dict["fields"] = row
                else:
                    rows.append(row)

        employees_dict["rows"] = rows
        return employees_dict

    except Exception as e:
        trace_back = traceback.extract_tb(e.__traceback__)
        stack_trace = []

        for trace in trace_back:
            stack_trace.append(
                f'File : {trace[0]} , Line : {trace[1]}, Func.Name : {trace[2]}, Message : {trace[3]}'
            )

        print(f"Exception type: {type(e).__name__}")
        message = str(e)
        if message:
            print(f"Exception message: {message}")

        print("Stack Trace:", stack_trace)
        exit()

employees = read_employees()

#Task 3

def column_index(column_name):
    return employees["fields"].index(column_name)


employee_id_column = column_index("employee_id")

#Task 4

def first_name(row_number):
    first_name_col = column_index("first_name")
    return employees["rows"][row_number][first_name_col]

#Task 5

def employee_find(employee_id):

    def employee_match(row):
        return int(row[employee_id_column]) == employee_id

    matches = list(filter(employee_match, employees["rows"]))
    return matches

# Task 6

def employee_find_2(employee_id):
    matches = list(
        filter(
            lambda row: int(row[employee_id_column]) == employee_id,
            employees["rows"],
        )
    )
    return matches

#Task 7

def sort_by_last_name():
    last_name_col = column_index("last_name")
    employees["rows"].sort(key=lambda row: row[last_name_col])
    return employees["rows"]


#Task 8

def employee_dict(row):
    result = {}
    fields = employees["fields"]

    for i, field in enumerate(fields):
        if field != "employee_id":
            result[field] = row[i]

    return result

#Task 9

def all_employees_dict():
    result = {}

    for row in employees["rows"]:
        emp = employee_dict(row)
        emp_id = row[employee_id_column]
        result[emp_id] = emp

    return result

#Task 10

import os

def get_this_value():
    return os.getenv("THISVALUE")

print(get_this_value())

#Task 11

import custom_module

def set_that_secret(new_secret):
    custom_module.set_secret(new_secret)

set_that_secret("my_new_secret")
print(custom_module.secret)

#Task 12

def read_csv_to_dict(filepath):
    try:
        with open(filepath, newline="") as f:
            reader = csv.reader(f)
            fields = next(reader)
            rows = [tuple(row) for row in reader]
        return {"fields": fields, "rows": rows}
    
    except Exception as e:
        trace_back = traceback.extract_tb(e.__traceback__)
        stack_trace = []

        for trace in trace_back:
            stack_trace.append(
                f'File : {trace[0]} , Line : {trace[1]}, Func.Name : {trace[2]}, Message : {trace[3]}'
            )

        print(f"Exception type: {type(e).__name__}")
        print(f"Stack trace: {stack_trace}")
        exit()

def read_minutes():
    minutes1 = read_csv_to_dict("../csv/minutes1.csv")
    minutes2 = read_csv_to_dict("../csv/minutes2.csv")
    return minutes1, minutes2

minutes1, minutes2 = read_minutes()

#Task 13

def create_minutes_set():
    set1 = set(minutes1["rows"])
    set2 = set(minutes2["rows"])
    return set1.union(set2)

minutes_set = create_minutes_set()

#Task 14

from datetime import datetime

def create_minutes_list():
    lst = list(minutes_set)

    converted = list(map(
        lambda x: (x[0], datetime.strptime(x[1], "%B %d, %Y")),
        lst
    ))

    return converted

minutes_list = create_minutes_list()

#Task 15

def write_sorted_list():
   
    sorted_list = sorted(minutes_list, key=lambda x: x[1])

    converted = list(map(
        lambda x: (x[0], x[1].strftime("%B %d, %Y")),
        sorted_list
    ))

    
    with open("./minutes.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(minutes1["fields"])  # header
        writer.writerows(converted)

    return converted

final_list = write_sorted_list()


