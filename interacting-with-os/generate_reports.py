#!/usr/bin/env python3
import os
import csv

def read_employees(csv_file_location):
    csv.register_dialect("empDialect", skipinitialspace=True, strict=True)
    employee_file = csv.DictReader(open(csv_file_location), dialect="empDialect")
    employee_list = []
    for data in employee_file:
        employee_list.append(data)
    return employee_list

def process_data(employee_list):
    department_list = []
    for employee_data in employee_list:
        department_list.append(employee_data["Department"])

    department_data = {}
    for department_name in department_list:
        department_data[department_name] = department_list.count(department_name)

    return department_data

def write_report(dictionary, report_file):
    with open(report_file, "+w") as f:
        for k in sorted(dictionary):
            f.write(str(k) + " : " + str(dictionary[k]) + "\n")
        f.close()

employee_list = read_employees("/home/student-00-aab15a8cda09/data/employees.csv")
dictionary = process_data(employee_list)

file_location = "/home/student-00-aab15a8cda09/data/report.txt"
write_report(dictionary, file_location)

#print(dictionary)
    #with open(csv_file_location) as csv_file:
        #file = csv.DictReader(csv_file)
        #file = csv.register_dialect("empDialect", skipinitialspace=True, strict=True)
