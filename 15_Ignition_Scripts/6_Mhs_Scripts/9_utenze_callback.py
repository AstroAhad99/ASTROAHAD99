# New Python Script to Generate NETWORK Blocks for Motors Based on Your Requirements

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

# Reverse lookup from Code to Channel
code_to_channel = {v: k for k, v in channel_mapping.items()}

# Script Variables
start_utenza = 101
start_photocell = 158

# Generate NETWORK Blocks
for utenza in range(101, 117):
    code = f"C2{utenza}"
    channel = code_to_channel.get(code, "UNKNOWN")

    is_odd = (utenza % 2) != 0

    if is_odd:
        ftc_testa = start_photocell
        ftc_coda = start_photocell + 1
        ftc_coda_line = f'FTC_CODA_T_SX               := "DB_WinCC_FOTOCELLULE".F[{ftc_coda}].FTC_FLT , // FOTOCELLULA DI CODA  (INGRESSO) FILTRATA (1=BGL)'
        ftc_testa_line = f'FTC_TESTA_T_DX              := "DB_WinCC_FOTOCELLULE".F[{ftc_testa}].FTC_FLT , // FOTOCELLULA DI TESTA (USCITA) FILTRATA (1=BGL)'
        safety_brk_line = f'SAFETY_BRK                  := "{code}_SEZ" , // UTENZA DISPONIBILE DA SAFETY BRAKER (NC)'
        start_photocell += 2
    else:
        ftc_testa = start_photocell
        ftc_coda_line = 'FTC_CODA_T_SX               := FALSE , // FOTOCELLULA DI CODA  (INGRESSO) FILTRATA (1=BGL)'
        ftc_testa_line = f'FTC_TESTA_T_DX              := "DB_WinCC_FOTOCELLULE".F[{ftc_testa}].FTC_FLT , // FOTOCELLULA DI TESTA (USCITA) FILTRATA (1=BGL)'
        safety_brk_line = 'SAFETY_BRK                  := TRUE , // UTENZA DISPONIBILE DA SAFETY BRAKER (NC)'
        start_photocell += 1

    network = f"""
NETWORK
TITLE = LANCIO MOTORE {code} -- {channel}
      CALL #_{code}
      (  N_UT                        := {utenza} , // NUMERO UTENZA
         RUN_AV_DX                   := \"Ist_IV_101-200\"._{code}.WinCC.RUNNING_Ist , // STATO RUNNING AVANTI DESTRA o UNICO
         RUN_IND_SX                  := FALSE , // STATO RUNNING INDIETRO SINISTRA
         {ftc_coda_line}
         {ftc_testa_line}
         CONCATENATO                 := FALSE , // 1= CONCATENATO CON NASTRO A VALLE (COME PROLUNGA es.CURVA)
         {safety_brk_line}
         READY                       := \"Ist_IV_101-200\"._{code}.WinCC.RDY_INVERTER , // READY ELETTRICO UTENZA (0=ALL)
         EMERG_HW_PCE                := \"WORK_Safety\".CONS_ELTN_EM_L2 , // STATO DI EMERGENZA HW (0=ALL)
         EMERG_SW_PAL                := TRUE , // PULSANTE DI ARRESTO LOCALE  EMERG_SW  (1=OK)
         PB_ATTRAV_PFL               := FALSE , // PULSANTE ARRESTO PER ATTRAVERSAMENTO (1=ARR)
         FEEDBACK_EXIST              := FALSE , // ABILITAZIONE TIME-OUT Esiste FEEDBACK RUNNING
         TIME_EMPTY_mm               := 30000.0 , // SPAZIO PER DEFINIZIONE NASTRO VUOTO mm (0=ANNULLA)
         TIME_PRESTART               := T#0MS , // TEMPO DURATA TENSIONE DI VIA (0=ANNULLA)
         SPEED_NST                   := \"Ist_IV_101-200\"._{code}.WinCC.ACT_SPEED , // VELOCITA NASTRO IN mm/Sec
         COM_UTENZA                  := #_{code}.APP_COM   // COMANDO UTENZA  (AV o IND in base SEL_DIR_REV)
      );
"""

    print(network)