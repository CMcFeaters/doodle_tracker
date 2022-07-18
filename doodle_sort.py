#test file for python code

import os
import sys
import datetime

path="/mnt/raid1/shared/doodle/"

list_dir=os.listdir(path)
rec_file=sorted(list_dir)

print(rec_file[len(rec_file)-1])
#print("hi")


