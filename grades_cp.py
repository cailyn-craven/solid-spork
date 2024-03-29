# I need to add some comments to say what I was doing in this file
#!/usr/bin/env python3
# Cailyn Craven
# With this package, we can work with arguments from the command line.
import sys
from operator import itemgetter
# This file needs at least one argument to run.
argc = len(sys.argv)
if argc == 1:
    print("Usage: ./grades.py filename")
else:
    with open(sys.argv[1], "r") as f:
        lines = [line.split(' ') for line in f]
        for line in sorted(lines, key=itemgetter(2,1,0)):
            grades = line[3:]
            #print(grades)
            total = 0 
            for grade in grades:
                total = total + int(grade)
            avg = total // 3
            print(avg,"["+ line[0]+ "]", line[2] + ",", line[1])
