# https://www.101daysofdevops.com/courses/101-days-of-devops/lessons/day-2-2/
 
# Day 2 – Python Script to check if the file or directory exists

import os
filename="C:\Ramkishor.ch\D\GITHUBB\Functions_Python\Python_Devops\Python_Devops\abc.txt"

if os.path.exists(filename) and os.path.isfile(filename):
    print("File exist")
else:
    print("File doesn't exist")