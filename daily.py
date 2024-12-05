import os
import hashlib
import requests
import time
import json

def download_image():
    url = 'https://www.mflan.com/dailyfilepost.jpg'
    response = requests.get(url)
    if response.status_code == 200:
        with open('temp.jpg', 'wb') as file:
            file.write(response.content)
    else:
        print(f"Failed to download image. Status code: {response.status_code}")

def calculate_md5(file_path):
    hash_md5 = hashlib.md5()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

def read_checksums():
    if os.path.exists('checksums.txt'):
        with open('checksums.txt', 'r') as file:
            return json.load(file)
    return {}

def save_checksums(checksums):
    with open('checksums.txt', 'w') as file:
        json.dump(checksums, file)

def process_image():

    if not os.path.exists('dailyfileposts'):
        os.makedirs('dailyfileposts')

    download_image()

    temp_md5 = calculate_md5('temp.jpg')

    checksums = read_checksums()

    if temp_md5 in checksums.values():
        print("Image already exists. Deleting temp.jpg.")
        os.remove('temp.jpg')  
    else:

        if checksums:
            last_no = max([int(key) for key in checksums.keys()])
        else:
            last_no = 0

        new_no = last_no + 1
        new_filename = f'dailyfileposts/dailyfilepost{new_no}.jpg'

        os.rename('temp.jpg', new_filename)

        checksums[str(new_no)] = temp_md5

        save_checksums(checksums)

        print(f"New image saved as {new_filename}.")

while True:
    process_image()
    time.sleep(3600)  