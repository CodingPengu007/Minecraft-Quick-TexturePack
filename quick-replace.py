import os

image_file = input("Enter the name of the .png image file: ")

if not os.path.exists(image_file):
    print("Error: File not found")
    input("Press Enter to exit...")
    exit()

folder = input("Enter the name of the folder: ")

if not os.path.exists(folder):
    print("Error: Folder not found")
    input("Press Enter to exit...")
    exit()

for root, dirs, files in os.walk(folder):
    for file in files:
        if file.endswith(".png"):
            file_path = os.path.join(root, file)
            with open(file_path, 'wb') as f:
                with open(image_file, 'rb') as img:
                    f.write(img.read())
            print(f"Replaced {file_path} with {image_file}")

print("")
input("Press Enter to exit...")
