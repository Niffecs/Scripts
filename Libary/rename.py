import os
import sys
import base64

# Codec Libary
libary_name = b'KWdyby5iaWwteig='
libary_name = base64.b64decode(libary_name).decode('utf-8')[::-1]

# Path
path_dir = "."
path_dir = path_dir.replace("\\", "//")

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
            "ü", "ue").replace("ß", "ss").replace("•", "")
        os.rename(f"{path_dir}//{flag}", f"{path_dir}//{runner}")

# Delete Author
runner = False
for runner in os.listdir(path_dir):
    if not ".py" in runner:
        start = runner.find("(")
        if ".pdf" in runner:
            new_name = f"{runner[0:start]}.pdf"
        elif ".epub" in runner:
            new_name = f"{runner[0:start]}.epub"
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
        else:
            print(f"Error\n\t-->\t{runner}")
        runner = runner.replace(" ", "_")
        os.rename(f"{path_dir}//{flag}", f"{path_dir}//{runner}")

# delete double Ends
runner = False
for runner in os.listdir(path_dir):
    if not ".py" in runner:
        flag = runner
        if ".pdf" in runner:
            runner = runner.replace("pdf", "")
            runner += ".pdf"
        elif ".epub" in runner:
            runner = runner.replace("epub", "")
            runner += ".epub"
        else:
            print(f"Error\n\t-->\t{runner}")
        runner = runner.replace(" ", "_")
        os.rename(f"{path_dir}//{flag}", f"{path_dir}//{runner}")
