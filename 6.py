import os

files = os.listdir() 
print(files)

for file in files:
    if os.path.isfile(file):
        print(file)
    
for folder in files:
    if not os.path.isfile(folder):
        print(folder)
