# https://www.101daysofdevops.com/courses/101-days-of-devops/lessons/day-3-2/
# Day 3 – A python script to search for a file

# Approach 1
# import os

# for dirpath, dirname, filename in os.walk("C:/Ramkishor.ch/D/GITHUBB/Functions_Python/Python_Devops/Python_Devops"):
#     for file in filename:
#         comp_path= os.path.join(dirpath,file)
#         if file == "test.txt":
#             print(comp_path)

# Approach 2
import argparse
import os
my_parser = argparse.ArgumentParser(description='Reading the directory path to find the file')
my_parser.add_argument("pathname", help='Please enter the directory path ')
my_parser.add_argument("filesearch", help='Please enter the filename to search')

args = my_parser.parse_args()
print(args)
for dirpath, dirname, filename in os.walk(args.pathname):
    for file in filename:
        comp_path= os.path.join(dirpath,file)
        if file == args.filesearch:
            print(comp_path)

# command to run : python filename.py directoryname filename.txt


