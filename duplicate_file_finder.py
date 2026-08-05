import hashlib
from pathlib import Path

def file_hash(path):
    hasher = hashlib.md5()
    with open(path, "rb") as file:
        hasher.update(file.read())
    return hasher.hexdigest()

folder = Path(".")

hashes = {}

for file in folder.rglob("*"):
    if file.is_file():
        h = file_hash(file)
        if h in hashes:
            print(f"Duplicate found: {file} == {hashes[h]}")
        else:
            hashes[h] = file
