# Using the OS module to manipulate paths
# For many applications, your Python code should work reliably independent of the particular OS for the file systems. In this case, you may wish to considering use the methods from the os module described below to create truly OS-independent Python code for manipulating paths. (Remember to \color{red}{\verb|import os|}importos before using these methods.)

# os.getcwd() returns the path to the current working directory for your Python code.
# os.path.abspath(file_name) returns to the absolute path the specified file.
# os.path.join(path,dir1,dir2,...,file_name) returns the absolute path to the file 
# file_name that lies in the sequence of nested directories 
# os.pardir returns the relative path to the parent directory of the current working directory. For most systems, this path is \color{red}{\verb|".."|}".."
# For examples of these methods in action, explore this path manipulation code. Since this code manipulates your file system, the code must be run on your desktop.
import os
print(os.getcwd())
print(os.pardir)
print(os.path.abspath("Desktop/../sai.py"))


wrk_dir = os.path.abspath("../Sach")

test_file = os.path.join(os.getcwd(),"Desktop","tets.py")
print(test_file)
# test1= open(test_file,"rt")
# data = test1.read()
# print(data)
# test1.close()