import os

# print(dir(os)) # Output : prints the attributes and methods supported by os module

# print(help(os)) # want to know about particular module in detail use help


# execute the os module in windows instead of linux, can use os module in python


print(os.listdir()) # Output : prints all list of directories/files

print(os.getcwd()) # Output : print current working directory

# print(os.mkdir("test_dir")) # Output : create a directory of name test_dir

# print(os.makedirs("test3/test4")) # Output : create recursive directories like test3 and inside test3 dir create test3

# print(os.chdir("test3/test4")) # Output : changing from test3 dir to test4 dir

# print(os.environ) # Output : print all environment variables

# print(os.rmdir("test_dir")) # Output : remove a directory

# print(os.removedirs("test3/test4")) # Output : remove a directory recursively

# print(os.rename("List_all_VPC.py","List_VPC.py")) # Output : rename a file

# print(os.path.basename("/GITHUBB/Functions_Python")) # Output : prints final component of the path

# print(os.path.dirname("/GITHUBB/Functions_Python")) # Output : prints directory component of the path

# print(os.path.getsize("C:\Ramkishor.ch\D\GITHUBB\Functions_Python")) # Output: prints bytes in size of the path

# print(os.path.exists("C:\Ramkishor.ch\D\GITHUBB\Functions_Python")) # Output : prints true/false whether that path exists or not

# print(os.path.isfile("C:\Ramkishor.ch\D\GITHUBB\Functions_Python"))  # Output : prints true/false whether it is file or not

# print(list(os.walk("C:\Ramkishor.ch\D\GITHUBB\Functions_Python"))) # Output : print the directory tree and all the files within that directory tree,