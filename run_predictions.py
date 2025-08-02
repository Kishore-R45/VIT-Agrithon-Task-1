import subprocess
import os
import csv
import time

# Paths
disease_script = os.path.join("disease", "some.py") 
insect_script = os.path.join("insects", "naga.py") 
disease_csv = os.path.join("disease", "predict_disease.csv")
insect_csv = os.path.join("insects", "predict_insect.csv")

# Step 1: Run prediction scripts
try:
    print("Running disease prediction script...")
    subprocess.run(["python", disease_script], check=True)

    print("Running insect prediction script...")
    subprocess.run(["python", insect_script], check=True)
except subprocess.CalledProcessError as e:
    print(f"❌ Error running prediction script: {e}")
    exit(1)

# Step 2: Wait until both CSV files exist
time.sleep(1)  # brief delay in case files are just being written

if not os.path.exists(disease_csv):
    print("❌ Disease prediction CSV not found!")
    exit(1)

if not os.path.exists(insect_csv):
    print("❌ Insect prediction CSV not found!")
    exit(1)

# Step 3: Read CSVs
def read_predictions(csv_path):
    preds = {}
    with open(csv_path, newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            if row and len(row) >= 2:
                image_name = row[0].strip()
                try:
                    prediction = int(row[1].strip())
                    preds[image_name] = prediction
                except ValueError:
                    continue  # skip header or bad data
    return preds

disease_preds = read_predictions(disease_csv)
insect_preds = read_predictions(insect_csv)

# Step 4: Merge results
x = []
image_names = sorted(set(disease_preds) | set(insect_preds))

for image in image_names:
    da = disease_preds.get(image, 0)
    ib = insect_preds.get(image, 0)

    if da == 1 and ib == 1:
        label = "Disease & Insect"
    elif da == 1:
        label = "Only Disease"
    elif ib == 1:
        label = "Only Insect"
    else:
        label = "None"

    x.append((image, label))
    print(f"{image}: {label}")

# Step 5: Save to final_output.csv
with open("final_output.csv", "w", newline='') as f:
    writer = csv.writer(f)
    writer.writerow(["Image", "Final Prediction"])
    writer.writerows(x)

print("✅ Final output written to final_output.csv")