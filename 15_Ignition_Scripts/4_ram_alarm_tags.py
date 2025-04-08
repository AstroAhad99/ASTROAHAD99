import json
import pandas as pd

# File paths
excel_path = r"C:\Users\Qanare\Documents\ASTROAHAD99\15_Ignition_Scripts\Alarms.xlsx"
json_template_path = r"C:\Users\Qanare\Documents\ASTROAHAD99\15_Ignition_Scripts\5_tags.json"
output_json_path = r"C:\Users\Qanare\Documents\ASTROAHAD99\15_Ignition_Scripts\generated_alarm_tags.json"

# Read relevant columns: F (5), G (6), I (8)
df = pd.read_excel(excel_path, usecols="F,G,I", header=None)
df.columns = ["label", "name", "path"]  # Rename columns for clarity

# Drop rows with empty 'name'
df = df.dropna(subset=["name"])

# Load the template JSON file
with open(json_template_path, "r") as f:
    json_data = json.load(f)

# Use the first tag in the template as a base
template_tag = json_data["tags"][0]

# Generate new tags from Excel data
new_tags = []
for _, row in df.iterrows():
    tag = json.loads(json.dumps(template_tag))  # Deep copy to avoid mutation
    tag["name"] = row["name"]
    tag["opcItemPath"] = f"ns=1;s=[CP1000]{row['path']}"
    
    # Replace the label inside the alarms list (assumes only one alarm per tag)
    if "alarms" in tag and len(tag["alarms"]) > 0:
        tag["alarms"][0]["label"] = row["label"]
    
    new_tags.append(tag)

# Final JSON structure
final_json = {"tags": new_tags}

# Write to output file
with open(output_json_path, "w") as f:
    json.dump(final_json, f, indent=2)

print(f"✅ Tag JSON with name, label, and opcItemPath customized: {output_json_path}")
