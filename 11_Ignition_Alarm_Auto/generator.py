import pandas as pd
import json
import os
import re

# Load the Excel file
excel_file = r'C:\Users\Qanare\Documents\ASTROAHAD99\11_Ignition_Alarm_Auto\AlarmsDematic.xlsx'
df = pd.read_excel(excel_file, sheet_name='Sheet1', header=2)  # Starts from row 3

# Initialize the JSON structure
json_data = {
    "name": "1_All_Alarms",
    "parameters": {
        "PLCname": {
            "dataType": "String"
        }
    },
    "tagType": "UdtType",
    "tags": []
}

# Iterate over each row to build the JSON structure
for index, row in df.iterrows():
    if len(row) < 6:
        print("Warning: Row does not contain enough columns.")
        continue
    
    # Process alarm name
    alarm_name = row.iloc[2]
    alarm_name = re.sub(r'\[(\d+)\]', r'\1', alarm_name)  # Replace [number] with just number
    alarm_name = alarm_name.replace('+', '_').replace('-', '_')  # Replace + and - with _

    # Add numbering in front of the alarm name (index starts at 1)
    alarm_name = f"{index + 1}_{alarm_name}"

    # Process alarm label
    alarm_label = row.iloc[4] if pd.notna(row.iloc[4]) else alarm_name
    
    # Process address
    address = row.iloc[5]
    cleaned_address = address.replace('%', '').replace('.', ',').replace('[', '').replace(']', '')
    formatted_address = f"[{{PLCname}}]{cleaned_address}"
    
    # Create the tag dictionary for this alarm
    tag = {
        "opcItemPath": {
            "bindType": "parameter",
            "binding": formatted_address
        },
        "valueSource": "opc",
        "dataType": "Boolean",
        "alarms": [
            {
                "setpointA": 1.0,
                "name": "Alarm",
                "label": alarm_label,
                "priority": "High"
            }
        ],
        "name": alarm_name,
        "tagType": "AtomicTag",
        "opcServer": "Ignition OPC UA Server"
    }
    
    # Append the tag to the tags list
    json_data["tags"].append(tag)

# Define the output path in the same folder as the script
output_path = os.path.join(os.path.dirname(excel_file), 'output.json')

# Convert the JSON structure to a JSON string and save it to a file
json_output = json.dumps(json_data, indent=2, ensure_ascii=False)
with open(output_path, 'w', encoding='utf-8') as f:
    f.write(json_output)

print(f"JSON data has been successfully written to '{output_path}'.")
