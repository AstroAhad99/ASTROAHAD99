# Mapping list: (Channel, Code)
mapping = [
    ("B2.CH67.01", "C2101"), ("B2.CH67.02", "C2102"),
    ("B2.CH68.01", "C2103"), ("B2.CH68.02", "C2104"),
    ("B2.CH69.01", "C2105"), ("B2.CH69.02", "C2106"),
    ("B2.CH70.01", "C2107"), ("B2.CH70.02", "C2108"),
    ("B2.CH71.01", "C2109"), ("B2.CH71.02", "C2110"),
    ("B2.CH72.01", "C2111"), ("B2.CH72.02", "C2112"),
    ("B2.CH73.01", "C2113"), ("B2.CH73.02", "C2114"),
    ("B2.CH74.01", "C2115"), ("B2.CH74.02", "C2116")
]

# Starting values
start_azion = 101
start_area = 2654

# Template text
network_template = """
NETWORK
TITLE = G120C GESTIONE INVERTER {code}-- {channel}
      CALL #_{code}// FAULT INVERTER
      (  N_AZION                     := {azion} , // NUMERO AZIONAMENTO MOTORE (superv)
         CANALE                      := \"{canale}_Telegram\" , // ADDRESS PERIFERIA PZD I/O (stessi indirizzi)
         IN_MANUALE                  := FALSE , // STATO DI MANUALE (1=MANUALE)
         IN_AUTOMATICO               := TRUE , // STATO DI AUTOMATICO (1=AUTOMATICO)
         START_STOP_AZION            := \"DB141_LGK_M\"._{code}.Q_Rip_COM_AVA_o_IND , // <- START/STOP AUTOM o MANUALE
         SEL_DIR_INV                 := TRUE , // INVERSIONE SEGNO DEL SET POINT
         DIREZ_PULS_MANU             := \"DB141_LGK_M\"._{code}.Q_Rip_COM_IND_SX , // DIREZIONE INVERSA IN MODALITA MANUALE (1=INVERSA)
         NO_RAMPA_Stop               := \"DB141_LGK_M\"._{code}.I_NO_Rampa_STOP , // ANNULLAMENTO RAMPA DI STOP
         RESET_FAILURE               := \"ACK\" , // RESET ACK
         CONSENSO_M                  := TRUE , // CONSENSO PER START (From POWER EMERGENCY)
         CLOCK_READ_DATA             := \"CICLOM_10\" , // CLOCK LETTURA DATI
         AREA_Inp_Out                := {area} , // AREA DEPOSITO INPUT/OUTPUT MORSETTIERE A BORDO CU (1 BYTE)
         RANGE_MAX_Vel               := 365.11 , // RIFERIMENTO VELOCITA MASSIMA (P2000) mm/sec
         RANGE_MAX_Torq              := 15.0 , // COPPIA AZIONAMENTO IN Nm COME NEL PARAM (P2003)
         RANGE_MAX_Corr              := 5.0 , // CORRENTE AZIONAMENTO IN Amp COME NEL PARAM  (P2002)
         LIM_MIN_RUN                 := 40.0 , // LIMITE MINIMO PER DEFINIZIONE DI RUNNING
         LIM_MIN_SPEED               := 0.0 , // LIMITE MINIMO VALORE VELOCITA mm/sec
         LIM_MAX_SPEED               := 1400.0 , // (75 HZ)LIMITE MASSIMO VALORE VELOCITA mm/sec
         RAMP_ACC                    := T#100MS , // RAMPA ACCELERAZIONE
         RAMP_DEC                    := T#100MS , // RAMPA DECELERAZIONE
         SET_POINT_SPEED_A           := \"@Work_r\".RIF_VEL_{code} , // SET POINT SPEED AUTOMATICO DA LOGICA
         SET_POINT_SPEED_M           := 500.0 , // SET POINT SPEED MANUALE DA WinCC
         RUNNING                     := \"DB141_LGK_M\"._{code}.I_RUNNING_DA_INVERTER , // RUNNING (AV o IND) ASSE
         OUT_RUNN_Nst                := \"DB141_LGK_M\"._{code}.I_RUNNING_Speed , // USCITA NASTRO IN MARCIA  (RUNNING + SPEED NASTRO)
         FAILURE                     := \"DB141_LGK_M\"._{code}.I_ALL_INVERTER
      );
"""

# Generate all networks
for idx, (channel, code) in enumerate(mapping):
    azion = start_azion + idx
    area = start_area + idx
    canale = channel.split(".", 1)[1]  # Example: CH67.01
    
    network = network_template.format(
        code=code,
        channel=channel,
        azion=azion,
        canale=canale,
        area=area
    )
    print(network)
