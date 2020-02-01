import sys
import os
import re

search = " ".join(sys.argv[1:-1])

if not search:
    exit("No search provided")

replace = sys.argv[-1]

files = os.listdir()

align = len(max(files, key=len))

for file in files:
    print(f"{file:<{align}} -> {re.sub(search, replace, file)}")

if not input("Ok? (y/n) ").startswith("y"):
    exit()

for file in files:
    new = re.sub(search, replace, file)
    if new != file:
        os.rename(file, new)
