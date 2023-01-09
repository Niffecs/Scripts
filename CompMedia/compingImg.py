import os
import hashlib
import sys

def remove_duplicate_images(folder_path):
    # First all image files in the folder are read in
    image_files = [f for f in os.listdir(folder_path) if f.endswith(".jpg") or f.endswith(".png") or f.endswith(".jpeg")]
    
    # A hash value is calculated for each image
    image_hashes = {}
    for file in image_files:
        with open(os.path.join(folder_path, file), "rb") as f:
            hash = hashlib.sha256(f.read()).hexdigest()
            
            if hash in image_hashes:
                os.remove(os.path.join(folder_path, file))
            else:
                image_hashes[hash] = file

remove_duplicate_images(sys.argv[1])
