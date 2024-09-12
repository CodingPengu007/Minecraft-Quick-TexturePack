import os

image_file = input("Enter the name of the image file: ")

if not os.path.exists(image_file):
    print("Error: File not found")
    input("Press Enter to exit...")
    exit()

folder = input("Enter the name of the folder: ")

if not os.path.exists(folder):
    print("Error: Folder not found")
    input("Press Enter to exit...")
    exit()

target_file = input("Enter the name of the image file to replace: ")

for root, dirs, files in os.walk(folder):
    for file in files:
        if file == target_file:
            file_path = os.path.join(root, file)
            if file_path != image_file:
                with open(file_path, 'wb') as f:
                    with open(image_file, 'rb') as img:
                        f.write(img.read())
                print(f"Replaced {file_path} with {image_file}")
            else:
                print(f"Error: Cannot replace {image_file} with itself")

print("")
input("Press Enter to exit...")