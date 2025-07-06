import os

# Main dataset folder
base_dir = "rock_dataset"

# Subfolders
subdirs = [
    "images/train",
    "images/val",
    "labels/train",
    "labels/val"
]

# Create folders
for subdir in subdirs:
    path = os.path.join(base_dir, subdir)
    os.makedirs(path, exist_ok=True)
    print(f"Created: {path}")

print("\n✅ Folder structure is ready! Now add images and labels.")
