import os

# Mapping from channel to conveyor codes
channel_mapping = [
    ("B2.CH67.01", "C2101"), ("B2.CH67.02", "C2102"),
    ("B2.CH68.01", "C2103"), ("B2.CH68.02", "C2104"),
    ("B2.CH69.01", "C2105"), ("B2.CH69.02", "C2106"),
    ("B2.CH70.01", "C2107"), ("B2.CH70.02", "C2108"),
    ("B2.CH71.01", "C2109"), ("B2.CH71.02", "C2110"),
    ("B2.CH72.01", "C2111"), ("B2.CH72.02", "C2112"),
    ("B2.CH73.01", "C2113"), ("B2.CH73.02", "C2114"),
    ("B2.CH74.01", "C2115"), ("B2.CH74.02", "C2116")
]

# Template for each network
network_template = """
NETWORK
TITLE = LANCIO BANCO CH{ch_id}: {conv1} -> {conv2} -> B{b_code}
      SET                        // ==== RUN VALLE === 
      A     "DB141_LGK_M"._{conv2}.Q_Rip_RUNN_AV_IND// <- RUNNING NASTRO A VALLE (dopo)
      O(
      A     "{conv1}_PB_ROSSO"      // <- PULSANTE BLOCCO ROSSO     (Pulsantiera Desk)
      AN    "{conv1}_BF1"           // <- FOTOCELLULA BF1 INIZIO NASTRO 1 (1=PRES OBJ)
      )
      =     "DB141_LGK_M"._{conv1}.I_STATO_RUN_VALLE// <- RUNNING UTENZE A VALLE

      A(
      A     "DB141_LGK_M"._B{b_code}.Q_Rip_RUNN_AV_IND// <- RUNNING NASTRO A VALLE (dopo)
      AN    "DB141_LGK_M"._{conv2}.I_SEL_DIR_REV// <- SELEZIONE MOVIMENTO INDIETRO (1=Reverse)
      O
      A     "DB141_LGK_M"._{conv1}.Q_Rip_RUNN_AV_IND// <- RUNNING NASTRO A VALLE (dopo)
      A     "DB141_LGK_M"._{conv1}.I_SEL_DIR_REV// <- SELEZIONE MOVIMENTO INDIETRO (1=Reverse)
      A     "DB141_LGK_M"._{conv2}.I_SEL_DIR_REV// <- SELEZIONE MOVIMENTO INDIETRO (1=Reverse)
      )
      =     "DB141_LGK_M"._{conv2}.I_STATO_RUN_VALLE// <- RUNNING UTENZE A VALLE
"""

# Generate all networks
output_text = ""

# Process two conveyors at a time
for i in range(0, len(channel_mapping), 2):
    ch_num = 67 + (i // 2)
    conv1 = channel_mapping[i][1]
    conv2 = channel_mapping[i+1][1]

    # B249 for C2101-C2112, B250 for C2113-C2116
    if conv1 in ["C2101", "C2103", "C2105", "C2107", "C2109", "C2111"]:
        b_code = 249
    else:
        b_code = 250

    network = network_template.format(
        ch_id=ch_num,
        conv1=conv1,
        conv2=conv2,
        b_code=b_code
    )
    output_text += network + "\n"

# Write to txt file
with open("Banco_RunValle_CH67_to_CH74.txt", "w", encoding="utf-8") as f:
    f.write(output_text)

print("Text file 'Banco_RunValle_CH67_to_CH74.txt' generated successfully!")