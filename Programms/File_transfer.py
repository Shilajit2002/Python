import os
import shutil

music_dir = "D:\\Music"

# Iterate through subdirectories and move music files to the root of music_dir
for root, dirs, files in os.walk(music_dir):
    for file in files:
        if file.lower().endswith(('.mp3', '.wav', '.flac', '.ogg')):  # Adjust extensions as needed
            src_path = os.path.join(root, file)
            dst_path = os.path.join(music_dir, file)
            shutil.move(src_path, dst_path)

print("Music files moved successfully!")