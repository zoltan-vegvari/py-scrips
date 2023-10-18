import os
import time
import json
import shutil
from pathlib import Path

# List of common image file extensions
image_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.webp']

# List of common video file extensions
video_extensions = ['.mp4', '.avi', '.mov', '.mkv', '.wmv', '.flv', '.webm']

# Combine both lists into a single array
file_extensions = image_extensions + video_extensions

directory = ''

files = Path(directory).glob('*')
for file in files:
    
    fileNme, extension = os.path.splitext(str(file))

    if extension.lower() in file_extensions:
        print('file with extension found: ' + fileNme + extension)
    
        if os.path.exists(str(file) + '.json'):
            with open(str(file) + '.json') as f:
                jsonData = json.load(f)
                timestamp = jsonData["photoTakenTime"]["timestamp"]

            os.utime(str(file), (int(timestamp), int(timestamp)))
    #os.rename(str(file), '/mnt/smb_share/docker/nextcloud-data/zltn/files/Photos/' + file.name)
