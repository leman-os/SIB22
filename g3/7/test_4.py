import sys
import os

if (os.path.exists(str(sys.argv[1]))):
    if (os.path.isdir(str(sys.argv[1]))):
        print("Dir")
    else:
        print("File")
else:
    print("Not Exist")