import os
from cryptography.fernet import Fernet

files=[]

for file in os.listdir():
    if file =="voldemort.py":
        continue
    if os.path.isfile(file):
        files.append(file)
print(files)





