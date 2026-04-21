import csv

employees = []

with open("../csv/employees.csv", newline="") as file:
    reader = csv.reader(file)
    for row in reader:
        employees.append(row)

names = [row[1] + " " + row[2] for row in employees[1:]]

print(names)

names_with_e = [name for name in names if "e" in name.lower()]

print(names_with_e)