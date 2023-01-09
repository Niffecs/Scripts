import os
import hashlib
import sys
import uuid
import time

def format_image(folder_path=".") -> None:
    os.chdir(folder_path)
    for file in os.listdir():
       if ".py" not in file: 
        print(file,f"\t-->\t{file[0:-3:1]}png")
        layer = file[0:-3:1].replace(".","")
        os.rename(file,f"{layer}.png")
    sys.exit(0)

def remove_duplicate_images(folder_path=".") -> None:
    # Zunächst werden alle Bilddateien im Ordner eingelesen
    image_files = [f for f in os.listdir(folder_path) if f.endswith(".jpg") or f.endswith(".png") or f.endswith(".jpeg")]
    delete = []    
    # Für jedes Bild wird ein Hash-Wert berechnet
    image_hashes = {}
    for file in image_files:
        with open(os.path.join(folder_path, file), "rb") as f:
            hash = hashlib.sha256(f.read()).hexdigest()
            # Wenn es bereits ein Bild mit demselben Hash gibt, wird es gelöscht
            if hash in image_hashes:
                delete.append(file) # --> Test new Thread
                #os.remove(os.path.join(folder_path, file))
            else:
                image_hashes[hash] = file
                
    for runner in delete:
        os.remove(os.path.join(folder_path, runner))

def rename(pathx=".") -> None:
    # New Thread
    os.chdir(pathx)    
    a = [f for f in os.listdir(".") if f.endswith(".jpg") or f.endswith(".png") or f.endswith(".jpeg")]
    for runner in a:
        y = str(uuid.uuid4()).replace("-","")
        y = y[0:16:1]
        os.rename(runner,f"{y}.jpg")
        

if __name__ == "__main__":
    format_image(".")
    remove_duplicate_images(".")
    rename(".")
