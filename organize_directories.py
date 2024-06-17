import os
import shutil

current_dir = os.path.dirname(os.path.realpath(__file__))


file_mapping = {
    ("png", "jpg", "gif", "jpeg", "svg"): "Images",
    ("exe", "msi"): "Apps",
    ("mp4", "webm"): "Videos",
    ("pdf", "docx", "xlsx"): "Docs",
    ("txt"): "Notes",
    ("rar", "zip"): "Compressed",
}


for extensions, folder in file_mapping.items():
    if not os.path.exists(folder):
        os.mkdir(folder)


for filename in os.listdir(current_dir):
    filepath = os.path.join(current_dir, filename)

    if os.path.isfile(filepath):
        for extensions, folder in file_mapping.items():
            if filename.endswith(extensions):
                shutil.copy(filepath, folder)
                os.remove(filepath)
                print(f"Moved {filename} to {folder} folder")
                break
