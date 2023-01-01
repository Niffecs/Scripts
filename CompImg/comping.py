import os
import hashlib

def remove_duplicate_images(folder_path):
    # Zunächst werden alle Bilddateien im Ordner eingelesen
    image_files = [f for f in os.listdir(folder_path) if f.endswith(".jpg") or f.endswith(".png")]
    
    # Für jedes Bild wird ein Hash-Wert berechnet
    image_hashes = {}
    for file in image_files:
        with open(os.path.join(folder_path, file), "rb") as f:
            hash = hashlib.sha256(f.read()).hexdigest()
            # Wenn es bereits ein Bild mit demselben Hash gibt, wird es gelöscht
            if hash in image_hashes:
                os.remove(os.path.join(folder_path, file))
            else:
                image_hashes[hash] = file
