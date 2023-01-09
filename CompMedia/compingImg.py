import os
import hashlib
import sys
import uuid
import time
from PIL import Image

def format_image(folder_path="."):
    image_files = [f for f in os.listdir(folder_path) if f.endswith(".JPG") or f.endswith(".png") or f.endswith(".jpeg")]  
    for file in image_files:
        img_png = Image.open(file)
        y = str(uuid.uuid4()).replace("-","")[0:8:1]
        img_png.save(f"{file}_{y}.jpg")


def remove_duplicate_images(folder_path="."):
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

def rename(pathx="."):
    # New Thread
    os.chdir(pathx)    
    a = [f for f in os.listdir(".") if f.endswith(".jpg") or f.endswith(".png") or f.endswith(".jpeg")]
    for runner in a:
        y = str(uuid.uuid4()).replace("-","")
        y = y[0:16:1]
        os.rename(runner,f"{y}.jpg")
        
format_image(".")
remove_duplicate_images(".")
rename(".")


