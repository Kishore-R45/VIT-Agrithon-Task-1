import pandas as pd

# Load YOLO and TabNet predictions from Excel instead of CSV
yolo_df = pd.read_excel("disease_presence_labels.csv.xlsx")         # contains filename, label
tabnet_df = pd.read_excel("crop_disease_characteristics.csv.xlsx")  # contains filename, q1, q2..., label

# Rename for clarity
yolo_df = yolo_df.rename(columns={"label": "yolo_pred"})
tabnet_df = tabnet_df.rename(columns={"label": "tabnet_pred"})

# Keep only relevant columns
tabnet_df = tabnet_df[["filename", "tabnet_pred"]]

# Merge both predictions
merged = pd.merge(yolo_df, tabnet_df, on="filename", how="inner")

# Print final decision for each image
for _, row in merged.iterrows():
    filename = row["filename"]
    yolo = row["yolo_pred"]
    tabnet = row["tabnet_pred"]

    if yolo == 1 or tabnet == 1:
        print(f"{filename}: disease present")
    else:
        print(f"{filename}: disease NOT present")
