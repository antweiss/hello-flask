#! /bin/python
import fileinput
import sys


print("Build number is " + sys.argv[1])
for line in fileinput.input("application.py", inplace=True):
  print(line.replace('Hello World!', 'Hello World! - '+sys.argv[1]).rstrip())
