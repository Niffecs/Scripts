#!/usr/bin/env python

import os
import keyboard
import sys
from string import lower

"""
    Deathcounter for Streamer
"""
#  Global variables
__author__:str = "Niffecs"
__copyright__:str = "Copyright 2022, Niffecs"
__license__:str = "MIT"
__version__:str = "1.0.1"
__email__:str = f"{lower(__author__)}@gmail.com"


# Load Global Vars
# Field to increase counter.
counter: str = "e"
# Field to cancel the programme
end: str = "q"
# Path to the logger file
# Please enter the path with double backslash
pathsplit: list[str] = "C:\\Users\\Niffecs\\Desktop\\Leon\\counter.txt".split("\\")
# If no file is available, this is taken as the start value.
start: int = 30

# Testing the file name
filename = pathsplit[len(pathsplit) - 1]

# Compose the new path
pathnew: str = ""

# It is recommended that the file is not included here. Therefore, the for-each is modified.
for i in range(0, len(pathsplit) - 1):
    pathnew += pathsplit[i] + "\\"

# Change path
try:
    os.chdir(pathnew)
except Exception as e:
    print("The path is not available. Please check if you have made a mistake")
    print("Exception: " + e)
    sys.exit(0)
finally:
    print("Current folder: " + os.getcwd())

# Test if the file already exists
# If the file does not exist, it is created.
try:
    with open(pathsplit[len(pathsplit) - 1], encoding="utf-8") as f:
        f.write(str(start))
except IOError as file_error:
    print("File not accessible\n I am trying to create the file.")

# This is where the actual programme begins.
# The rest was actually just configuration stuff.
# That's why it's tied into an endless Loop.
while True:
    # Here is when the button is pressed.
    if keyboard.read_key() == counter:
        # Creating the File Handler
        with open(pathsplit[len(pathsplit) - 1], "r+", encoding="utf-8") as container:
            # Fix Byte Problems: \x00
            runner = int(f.readline().replace(" ", "").replace("\x00", ""))+1
            # Outpute
            print(f"Runner:{runner-1}\nType{type(runner)}", end="\n")
            # Emptying the file at byte level
            container.seek(0)
            # Describe the file with the new countere
            container.write(str(runner))

    # End of the Tsukuyomi
    if keyboard.read_key() == end:
        print("Programm end")
        break

# Exit the complete programme.
sys.exit(0)
