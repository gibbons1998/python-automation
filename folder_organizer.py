import shutil
from pathlib import Path

folder = Path(".")

folders = {
    ".jpg": "Images",
    ".png": "Images",
    ".pdf": "Documents",
    ".docx": "Documents",
    ".xlsx": "Spreadsheets",
    ".csv": "Spreadsheets",
}

for file in folder.iterdir():
    if file.is_file():
        destination = folders.get(file.suffix.lower())

        if destination:
            Path(destination).mkdir(exist_ok=True)
            shutil.move(str(file), str(Path(destination) / file.name))

print("Files organized successfully.")
