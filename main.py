import os
import hashlib
import shutil
from PIL import Image

def calculate_hash(image_path):
    """Calculate MD5 hash for an image file."""
    with Image.open(image_path) as img:
        hash_object = hashlib.md5(img.tobytes())
    return hash_object.hexdigest()

def find_and_move_duplicates(folder_path, delete_folder):
    """Find duplicate image files in the specified folder and move them to the delete folder."""
    hashes = {}
    if not os.path.exists(delete_folder):
        os.makedirs(delete_folder)

    for root, _, files in os.walk(folder_path):
        for file in files:
            if file.lower().endswith(('jpg', 'jpeg', 'png', 'gif', 'bmp')):
                file_path = os.path.join(root, file)
                try:
                    file_hash = calculate_hash(file_path)
                    if file_hash in hashes:
                        duplicate_path = os.path.join(delete_folder, file)
                        # Ensure the target path is unique in case of naming conflicts
                        base, extension = os.path.splitext(duplicate_path)
                        counter = 1
                        while os.path.exists(duplicate_path):
                            duplicate_path = f"{base}_{counter}{extension}"
                            counter += 1
                        shutil.move(file_path, duplicate_path)
                        print(f"Moved {file_path} to {duplicate_path}")
                    else:
                        hashes[file_hash] = file_path
                except Exception as e:
                    print(f"Error processing {file_path}: {e}")

# Define the paths
folder_path = 'photos'  # Path to the folder containing the images
delete_folder = os.path.join(folder_path, 'delete')  # Path to the delete folder

# Find and move duplicate files to the delete folder
find_and_move_duplicates(folder_path, delete_folder)
