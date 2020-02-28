import os
from datetime import datetime as dt

print(os.getcwd())
os.chdir("E:/")
print(os.getcwd())

os.chdir("D:/Python programs")
#print(os.listdir())
try:
    os.mkdir("OS_module_test")
except:
    pass

os.chdir("D:/Python programs/OS_module_test")
try:
    os.makedirs("D:/Python programs/OS_module_test/sub_1/sub_1_1")
    os.mkdir("D:/Python programs/OS_module_test/sub_2")
except:
    pass

try:
    os.rmdir("D:/Python programs/OS_module_test/sub_2")
except:
    pass

os.chdir('D:/Python programs/OS_module_test/sub_1/sub_1_1')
try:
    with open("sub_1_1.txt", "r+") as f:
        f.write("New file is created!")
        os.rename("sub_1_1.txt", "demo.txt")
except:
    with open("demo.txt", "r+") as f:
        f.write("New file is created!")
    print(os.stat('demo.txt'))
    print("Recent metadeta change at = ", dt.fromtimestamp(os.stat('demo.txt').st_ctime))
    print("Last modified = ", dt.fromtimestamp(os.stat('demo.txt').st_mtime))
    
    
for dirpath, dirnames, filenames in os.walk("E:/"):
    print("current Path = ", dirpath)
    print(os.path.split(dirpath))
    print("fileformat = ", os.path.splitext(dirpath))
    print("Movie name = ", os.path.basename(dirpath))
    print("Directories = ", dirnames)
    print("files = ", filenames)
    print("\n")
    
    
    
    
    
    
    
    
    