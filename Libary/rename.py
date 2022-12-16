# /usr/bin/env python3

# There is no beauty award or anything like that for the following source code.
# It fulfills the task I set for the source code.
# Since this is fulfilled, I am satisfied.
# As you can see, the code is written blockwise, so you can replace or extend certain blocks.
# I do not guarantee the correctness of the code written here.
# As said. It works for me, so be careful when you run it on your end.

import os
import sys
import base64

# Codec Libary
libary_name = b'KWdyby5iaWwteig='
libary_name = base64.b64decode(libary_name).decode('utf-8')[::-1]

# Path
path_dir = "."
path_dir = path_dir.replace("\\", "//")

for runner in os.listdir(path_dir):
	if ".htm" in runner:
        	layer = runner.replace("htm","pdf")
        	os.rename(f"{path_dir}//{runner}", f"{path_dir}//{layer}")

# Test Folder
error = 0
for runner in os.listdir(path_dir):
    if not "pdf" in runner:
        if not "epub" in runner:
            if not "py" in runner:
                error += 1
                print("Unbekannte Datei:\n")
                print(f"\t{runner}\n")
                print("Stop")
if error != 0:
    sys.exit(0)

# Delete end of File
for runner in os.listdir(path_dir):
    if not ".py" in runner:
        # Delete Libary ending
        os.rename(f"{path_dir}//{runner}",
                  f"{path_dir}//{runner}".replace(libary_name, ""))

# Rename Umlaute
runner = False
for runner in os.listdir(path_dir):
    if not ".py" in runner:
        flag = runner
        runner = runner.replace("ä", "ae").replace("ö", "oe").replace(
            "ü", "ue").replace("ß", "ss").replace("•", "").replace("™", "")
        os.rename(f"{path_dir}//{flag}", f"{path_dir}//{runner}")

# Delete Author
runner = False
for runner in os.listdir(path_dir):
    if not ".py" in runner:
        if ".pdf" in runner:
            new_name = f"{runner[0:runner.find('(')]}.pdf"
        elif ".epub" in runner:
            new_name = f"{runner[0:runner.find('(')]}.epub"
        else:
            print(f"Error\n\t-->{runner}")
            sys.exit(0)
        os.rename(f"{path_dir}//{runner}", f"{path_dir}//{new_name}")

# delete WhiteSpace
runner = False
for runner in os.listdir(path_dir):
    if not ".py" in runner:
        flag = runner
        if ".pdf" in runner:
            runner = runner.replace(" .pdf", ".pdf")
        elif ".epub" in runner:
            runner = runner.replace(" .epub", ".epub")
        runner = runner.replace(" ", "_")
        os.rename(f"{path_dir}//{flag}", f"{path_dir}//{runner}")

# delete double Ends
runner = False
for runner in os.listdir(path_dir):
    if not ".py" in runner:
        flag = runner
        if "pdf" in runner:
            end = ".pdf"
        else:
            end = ".epub"
        runner = f"{runner[0:runner.find('.')]}{end}"
        print(runner)
        os.rename(f"{path_dir}//{flag}", f"{path_dir}//{runner}")
