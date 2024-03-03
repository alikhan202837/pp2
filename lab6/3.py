import os

if os.path.exists(r"C:\Users\Asus\Desktop\pp2\lab6\folder\3.txt"):
    
    directory, file = os.path.split(r"C:\Users\Asus\Desktop\pp2\lab6\folder\3.txt")
    print("Directory name:", directory)
    print("File name:", file)

else:
    print("File not exists")