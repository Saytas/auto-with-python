#!/usr/bin/env python3

import sys
import subprocess

file_location = sys.argv[1]
file = open(file_location)

for line in file.readlines():
  line = line.strip()
  old_name = line
  new_name = old_name.replace('jane', 'jdoe')
  subprocess.run(['mv', old_name, new_name])
  #line = line[2]
  #print(line)
file.close()



#!/usr/bin/env python3
#import sys
#import subprocess
#
#f = open(sys.argv[1], "r")
#for line in f.readlines():
#  old_name = line.strip()
#  new_name = old_name.replace("jane", "jdoe")
#  subprocess.run(["mv", old_name, new_name])
#f.close()
