import pandas as pd
import os

# 🔄 Set the image name you are checking
image_name = "image1"  # Change this as needed

# ✅ TabNet prediction from CSV
tabnet_csv_path = "crop_insect_characteristics.csv"
df = pd.read_csv(tabnet_csv_path)

# Default value
insect_tabnet = 0

# Check if image exists and get its label
if image_name in df["filename"].values:
    insect_tabnet = int(df[df["filename"] == image_name]["label"].values[0])

# ✅ YOLO: check if a label .txt file exists (non-empty)
yolo_label_path = f"runs/detect/predict/labels/{image_name}.txt"
insect_yolo = 1 if os.path.exists(yolo_label_path) and os.path.getsize(yolo_label_path) > 0 else 0

# 🔚 Final Decision
if insect_yolo or insect_tabnet:
    print(f"✅ Final Output: Crop insect present in {image_name}")
else:
    print(f"✅ Final Output: Crop insect NOT present in {image_name}")
