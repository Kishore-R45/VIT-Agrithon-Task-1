import pandas as pd
import os

# Corrected path to where results.csv is actually present
csv_path = "C:/Users/Asus/Downloads/diseaseee/crop_disease_seg_model3/results.csv"

if not os.path.exists(csv_path):
    raise FileNotFoundError(f"File not found: {csv_path}")

df = pd.read_csv(csv_path)

exclude_columns = ['epoch', 'time']
columns_to_binarize = [col for col in df.columns if col not in exclude_columns]

df[columns_to_binarize] = df[columns_to_binarize].applymap(lambda x: 1 if x > 0 else 0)

output_path = os.path.join(os.path.dirname(csv_path), "results.csv")
df.to_csv(output_path, index=False)

print(f"Binary results saved at:\n{output_path}")
