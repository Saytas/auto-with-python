#!/usr/bin/env python3

import re
import csv
import operator

per_user = {}
error = {}

log_file = "/home/student-04-e47d6be59d7c/syslog.log"

with open(log_file, "r") as csv_file:
  for line in csv_file:
    pattern = r"ticky: ([\w]{4,5}) ([\w\s]+)[\[\]#\d\s]*\((\w*)"
    reg_ex = re.search(pattern, line)
    if reg_ex:
      log_type = reg_ex.group(1)
      error_message = reg_ex.group(2).strip()
      user = reg_ex.group(3)
      #print("log_type: ", log_type)
      #print("error_message: ", error_message)
      #print("user: ", user)
      if log_type == "ERROR":
        if error_message not in error.keys():
          error[error_message] = 0
        error[error_message] += 1
      if user not in per_user.keys():
        per_user[user] = {}
        per_user[user]["ERROR"] = 0
        per_user[user]["INFO"] = 0
      if log_type == "ERROR":
        per_user[user]["ERROR"] += 1
      elif log_type == "INFO":
        per_user[user]["INFO"] += 1
    #print(line)
csv_file.close()

per_user = sorted(per_user.items())
error = sorted(error.items(), key=operator.itemgetter(1), reverse=True)

error_messages_file = "error_message.csv"
user_statistics_file = "user_statistics.csv"


with open(error_messages_file, "w") as err_file:
  writer = csv.writer(err_file)
  writer.writerow(["Error", "Count"])
  writer.writerows(error)
err_file.close()

with open(user_statistics_file, "w") as usr_stat_file:
  writer = csv.writer(usr_stat_file)
  writer.writerow(["Username", "INFO", "ERROR"])
  for each in per_user:
    each_row = [each[0], each[1]["INFO"], each[1]["ERROR"]]
    writer.writerow(each_row)
usr_stat_file.close()
