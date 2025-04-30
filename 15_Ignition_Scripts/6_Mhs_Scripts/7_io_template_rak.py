import pandas as pd

# Mapping list: (Channel, Code)
mapping = [
    ("B2.CH67.01", "C2101"),
    ("B2.CH68.01", "C2103"),
    ("B2.CH69.01", "C2105"),
    ("B2.CH70.01", "C2107"),
    ("B2.CH71.01", "C2109"),
    ("B2.CH72.01", "C2111"),
    ("B2.CH73.01", "C2113"),
    ("B2.CH74.01", "C2115")
]

# Template for IO list
io_template = [
    ("_PB_GIALLO", "Bool", "False", "True", "True", "True", "PULSANTE GIALLO MANUALE"),
    ("_PB_BLU", "Bool", "False", "True", "True", "True", "PULSANTE BLU ETICHETTATURA"),
    ("_PB_VERDE", "Bool", "False", "True", "True", "True", "PULSANTE VERDE SPEDIZIONE AUTOMATICA"),
    ("_PB_ROSSO", "Bool", "False", "True", "True", "True", "PULSANTE ROSSO REVERSE MANUALE"),
    ("_EXTRAPESO", "Bool", "False", "True", "True", "True", "SEGNALE EXTRAPESO"),
    ("_SEZ", "Bool", "False", "True", "True", "True", "STATO SEZIONATORE CHIUSO"),
    ("_Ne_I16", "Bool", "False", "True", "True", "True", "Not Exist SU G120C"),
    ("_Ne_I11", "Bool", "False", "True", "True", "True", "Not Exist SU G120C"),
    ("_BF10", "Bool", "False", "True", "True", "True", "FTC CODA NASTRO BILANCIA {code}"),
    ("_BF1", "Bool", "False", "True", "True", "True", "FTC TESTA NASTRO BILANCIA {code}"),
    ("_BF1", "Bool", "False", "True", "True", "True", "FTC TESTA NASTRO TRASPORTO {code}"),
    ("_Ris", "Bool", "False", "True", "True", "True", "Riserva Cablata"),
    ("_S001", "Bool", "False", "True", "True", "True", "SENSORE SICUREZZA REVERSE NASTRO {code}"),
    ("_TERM", "Bool", "False", "True", "True", "True", "READY SCATTO INTERRUTTORI"),
    ("_Ne_I26", "Bool", "False", "True", "True", "True", "Not Exist SU G120C"),
    ("_Ne_I27", "Bool", "False", "True", "True", "True", "Not Exist SU G120C")
]

# Prepare data for DataFrame
data = []
byte = 2654
bit = 0

for (channel, code) in mapping:
    for suffix, datatype, defval, a, b, c, comment in io_template:
        address = f"%I{byte}.{bit}"
        row = [f"{code}{suffix}", datatype, address, defval, a, b, c, comment.replace("{code}", code)]
        data.append(row)
        bit += 1
        if bit > 7:
            bit = 0
            byte += 1

# Create DataFrame
df = pd.DataFrame(data, columns=["Tag", "DataType", "Address", "Default", "A", "B", "C", "Comment"])

# Save to Excel
output_file = "IO_List_Generated.xlsx"
df.to_excel(output_file, index=False)

print(f"Excel file '{output_file}' generated successfully!")