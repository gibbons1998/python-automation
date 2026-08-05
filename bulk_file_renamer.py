from pathlib import Path

folder = Path(".")

for index, file in enumerate(folder.iterdir(), start=1):
    if file.is_file():
        new_name = f"file_{index}{file.suffix}"
        file.rename(folder / new_name)

print("Files renamed successfully.")
