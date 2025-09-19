import cv2
import os

# 📥 Get user input
input_path = input("Enter the input image path (e.g., image.jpg): ").strip()
new_format = input("Enter new format (e.g., png, jpg, jpeg): ").strip().lower()
width = int(input("Enter new width: ").strip())
height = int(input("Enter new height: ").strip())

# 📤 Generate output path
base_name = os.path.splitext(os.path.basename(input_path))[0]  # remove extension
output_path = f"{base_name}_converted.{new_format}"

# 🖼️ Read the image
img = cv2.imread(input_path)

if img is None:
    print("❌ Error: Could not read the image. Check the path or file format.")
else:
    # Resize the image
    resized = cv2.resize(img, (width, height))
    # Save with new format
    cv2.imwrite(output_path, resized)
    print(f"✅ Saved converted image as: {output_path}")


