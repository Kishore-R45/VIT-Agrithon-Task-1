import os

# Path to the label files
label_folder = r"C:\Users\Asus\Downloads\diseaseee\runs\detect\predict3\labels"  # Change to your folder

output = []

for file in os.listdir(label_folder):
    if file.endswith(".txt"):
        path = os.path.join(label_folder, file)
        with open(path, "r") as f:
            lines = f.readlines()
            label = 1 if len(lines) > 0 else 0
            output.append((file.replace('.txt', ''), label))

# Save as CSV
with open("disease_presence_labels.csv", "w") as out_file:
    out_file.write("filename,label\n")
    for name, label in output:
        out_file.write(f"{name},{label}\n")

print("✅ Done: disease_presence_labels.csv generated.")
