import os
from testimg import identify_image
import sys

# Path of the folder whose files will be listed
folder_path = "example"
os.chdir(folder_path)

# Empty list where the files will be stored
file_list = []

# Loop through all the files in the folder
for file_name in os.listdir("."):
    # Add the file name to the list
    file_list.append(file_name)

# Print result
print(identify_image("image01.jpg"))

sys.exit(0)

for runner in file_list:
    print(f"{runner}\t-->\t{identify_image(runner)}")
