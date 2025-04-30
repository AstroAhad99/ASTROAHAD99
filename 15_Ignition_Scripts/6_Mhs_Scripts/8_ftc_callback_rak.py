# New Python Script to Generate NETWORK Blocks Based on Your Requirements

# Mapping from Channel to Code
channel_mapping = {
    "B2.CH67.01": "C2101",
    "B2.CH67.02": "C2102",
    "B2.CH68.01": "C2103",
    "B2.CH68.02": "C2104",
    "B2.CH69.01": "C2105",
    "B2.CH69.02": "C2106",
    "B2.CH70.01": "C2107",
    "B2.CH70.02": "C2108",
    "B2.CH71.01": "C2109",
    "B2.CH71.02": "C2110",
    "B2.CH72.01": "C2111",
    "B2.CH72.02": "C2112",
    "B2.CH73.01": "C2113",
    "B2.CH73.02": "C2114",
    "B2.CH74.01": "C2115",
    "B2.CH74.02": "C2116"
}

# List of FTC sensors
ftc_list = [
    "C2101_BF1", "C2101_BF10", "C2102_BF1",
    "C2103_BF1", "C2103_BF10", "C2104_BF1",
    "C2105_BF1", "C2105_BF10", "C2106_BF1",
    "C2107_BF1", "C2107_BF10", "C2108_BF1",
    "C2109_BF1", "C2109_BF10", "C2110_BF1",
    "C2111_BF1", "C2111_BF10", "C2112_BF1",
    "C2113_BF1", "C2113_BF10", "C2114_BF1",
    "C2115_BF1", "C2115_BF10", "C2116_BF1"
]

# Reverse lookup from Code to Channel
code_to_channel = {v: k for k, v in channel_mapping.items()}

# Script Variables
p_number = 158

# Generate NETWORK Blocks
for idx, ftc in enumerate(ftc_list):
    code, sensor = ftc.split("_")
    motor_number = code.replace("C2", "")
    m_number = int(motor_number)
    
    # Determine B2.CHxx.yy from code
    channel = code_to_channel.get(code, "UNKNOWN")

    network = f"""
NETWORK
TITLE = LANCIO \"{ftc}\" P{p_number:03} M{m_number} {channel}
      CALL #FTC_P{p_number:03}
      (  NR_FTC                      := {idx+158} , // NUMERO FOTOCELLULA
         Nr_MOT                      := {m_number} , // NUMERO MOTORE ASSOCIATO (0->Nessuno)
         FTC_DA_HW                   := \"{ftc}\" , // FOTOCELLULA HW DA FILTRARE
         FTC_Next                    := False , // INPUT NEXT PEC FILTRATA(1=BGL)
         TY_ZERO_BAG                 := TRUE , // TYPE 0= BAGAGLIO (1=SI 0=NO)
         BLC_NASTRO                  := TRUE , // ALLARME FTC BLOCCA NASTRO ? (1=SI 0=NO)
         FIL_INTERV_FTC_mm_o_T       := 20.0 , // FILTRO INTERVENTO FOTOCELLULE IN mm O Msec (RIT RILEVAZIONE OBJ)
         FIL_RILASC_FTC_mm_o_T       := 30.0 , // FILTRO RILASCIO FOTOCELLULE IN mm O Msec (RIT RILASCIO OBJ)
         TO_BLK_MONTE_FTC_mm         := 3000.0 , //SPAZIO DI TIME_OUT FOTOCELLULE TESTA/CODA PER BLOCCO A MONTE mm (0=ANNULLA)
         TO_POSS_JAM_mm              := 1500.0 , // SPAZIO DI TIME_OUT FOTOCELLULE TESTA/CODA PER POSSIBILE
         TO_ALL_FTC_mm               := 3000.0   //SPAZIO DI TIME_OUT FOTOCELLULE TESTA/CODA PER ALLARME NASTRO mm (0=ANNULLA)
      );
"""
    print(network)
    p_number += 1
