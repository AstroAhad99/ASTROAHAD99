import pandas as pd

# Define template tags
lamp_template = [
    ("_LAMP_BLU", "LAMPADA PULSANTE BLU"),
    ("_LAMP_GIALLO", "LAMPADA PULSANTE GIALLO"),
    ("_Ne_Q12", "Not Exist SU G120C"),
    ("_Ne_Q13", "Not Exist SU G120C"),
    ("_Ne_Q14", "Not Exist SU G120C"),
    ("_Ne_Q15", "Not Exist SU G120C"),
    ("_Ne_Q16", "Not Exist SU G120C"),
    ("_Ne_Q17", "Not Exist SU G120C"),
    ("_LAMP_ROSSO", "LAMPADA PULSANTE ROSSO"),
    ("_LAMP_VERDE", "LAMPADA PULSANTE VERDE"),
    ("_Ne_Q22", "Not Exist SU G120C"),
    ("_Ne_Q23", "Not Exist SU G120C"),
    ("_Ne_Q24", "Not Exist SU G120C"),
    ("_Ne_Q25", "Not Exist SU G120C"),
    ("_Ne_Q26", "Not Exist SU G120C"),
    ("_Ne_Q27", "Not Exist SU G120C")
]

# Initialize list to collect tag data
data = []

# Starting point
byte = 2654
bit = 0

# Loop through CH67 to CH74
for ch_num in range(67, 75):
    base_name = f"CH{ch_num}"
    for suffix, comment in lamp_template:
        address = f"%Q{byte}.{bit}"
        data.append([
            base_name + suffix,
            "Bool",
            address,
            "False",
            "True",
            "True",
            "True",
            "",
            comment
        ])
        bit += 1
        if bit > 7:
            bit = 0
            byte += 1

# Create a DataFrame
df = pd.DataFrame(data, columns=[
    "Tag", "DataType", "Address", "Default", "A", "B", "C", "", "Comment"
])

# Save to Excel
df.to_excel("Lamp_Tags_CH67_to_CH74.xlsx", index=False)

print("Excel file 'Lamp_Tags_CH67_to_CH74.xlsx' generated successfully!")
