import os

if os.path.exists("newfile.txt"):
    os.remove("newfile.txt")
else:
    print("file not exist")