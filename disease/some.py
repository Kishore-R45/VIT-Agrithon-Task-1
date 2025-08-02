import pandas as pd
import os

file_path1 = os.path.join(os.path.dirname(__file__), "disease_presence_labels.xlsx")
yolo_df = pd.read_excel(file_path1)

# Read the second Excel file
file_path2 = os.path.join(os.path.dirname(__file__), "crop_disease_characteristics.xlsx")
tabnet_df = pd.read_excel(file_path2)

yolo_df = yolo_df.rename(columns={"label": "yolo_pred"})
tabnet_df = tabnet_df.rename(columns={"label": "tabnet_pred"})

tabnet_df = tabnet_df[["filename", "tabnet_pred"]]

merged = pd.merge(yolo_df, tabnet_df, on="filename", how="inner")

for _, row in merged.iterrows():
    filename = row["filename"]
    yolo = row["yolo_pred"]
    tabnet = row["tabnet_pred"]

    if yolo == 1 or tabnet == 1:
        print(f"{filename}: disease present")
    else:
        print(f"{filename}: disease NOT present")
