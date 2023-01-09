#!/usr/bin/python
output = open("output.txt", "w")
file = open("list.txt", "r")
for line in file:
    if "/video/" in line:
        output.write(f"{line}")
file.close()
output.close()
