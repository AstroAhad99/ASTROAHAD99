# Python Script to Generate CALL #_CHXX Structure Dynamically

# Configuration for dynamic replacements
start_chk = 67
start_odd_motor = 2101
start_photocell = 158

# Template
structure_template = """
NETWORK
      CALL  #_CH{chk_id}
         NR              :={chk_id}    // <- NUMERO DI BANCO CHECK-IN
         ABILITAZ        :=TRUE  // <- ABILITAZIONE BANCO
         ACK             :=\"DB_WinCC_LINEE\".Line_L2.ACK_LINEA// <- SEGNALE ACK PER QUESTO BANCO
         LAMP_TEST       :=\"QCP_PB_LAMP_TEST\"// <- PULSANTE DI LAMP TEST
         START_LINEA     :=\"DB_WinCC_LINEE\".Line_L2.START_LINEA// START LINEA UTENZE
         ABIL_SUP_WinCC  :=\"DB_WinCC_LINEE\".Line_L2.ABILIT_SUPERVISIONE// <- ABILITAZIONE START DA WinCC (1=ABILITA)
         PB_GIALLO       :=\"{motor_code}_PB_GIALLO\"// <- PULSANTE MANUALE GIALLO
         PB_BLU          :=\"{motor_code}_PB_BLU\"// <- PULSANTE REVERSE BLU
         PB_VERDE        :=\"{motor_code}_PB_VERDE\"// <- PULSANTE SPEDIZIONE VERDE
         PB_ROSSO        :=\"{motor_code}_PB_ROSSO\"// <- PULSANTE BLOCCO ROSSO
         S1              :=TRUE  // <- SENSORE SICUREZZA S1 (0=ALLARME)
         BF1             :=\"DB_WinCC_FOTOCELLULE\".F[{bf2}].FTC_FLT// <- FOTOCELLULA BF1 INIZIO NASTRO 1
         BF2             :=\"DB_WinCC_FOTOCELLULE\".F[{bf1}].FTC_FLT// <- FOTOCELLULA BF2 FINE   NASTRO 1
         BF3             :=\"DB_WinCC_FOTOCELLULE\".F[{bf3}].FTC_FLT// <- FOTOCELLULA BF3 FINE   NASTRO 2
         OVERWEIGHT      :=\"{motor_code}_EXTRAPESO\"// <- SEGNALE DI SOVRAPPESO NASTRO 1
         RDY_no_ALM_01   :=\"DB141_LGK_M\"._{motor_code}.Q_Rip_RDY_AUT_noALARM// <- READY AUTOM NO ALARM 01
         RDY_no_ALM_02   :=\"DB141_LGK_M\"._{next_motor_code}.Q_Rip_RDY_AUT_noALARM// <- READY AUTOM NO ALARM 02
         SAFETY_BREAK    :=\"{motor_code}_SEZ\"// <- STATO SEZIONATORE
         INTERR_AUT      :=\"{motor_code}_TERM\"// <- STATO INTERRUTTORI AUTOMATICI
         LAMP_QU_BIANCA  :=#APP_out_LB
         LAMP_PB_GIALLA  :=\"CH{chk_id}_LAMP_GIALLO\"
         LAMP_QU_GIALLA  :=#APP_out_LG
         LAMP_PB_BLU     :=\"CH{chk_id}_LAMP_BLU\"
         LAMP_PB_ROSSA   :=\"CH{chk_id}_LAMP_ROSSO\"
         LAMP_PB_VERDE   :=\"CH{chk_id}_LAMP_VERDE\"
         ABIL_STA_NST_01 :=\"DB141_LGK_M\"._{motor_code}.I_ABIL_START_LINEA
         ABIL_STA_NST_02 :=\"DB141_LGK_M\"._{next_motor_code}.I_ABIL_START_LINEA
         SPEED_NST_01    :=\"@Work_r\".RIF_VEL_{motor_code}
         SPEED_NST_02    :=\"@Work_r\".RIF_VEL_{next_motor_code}
         PRENOTAZIONE    :=\"@WORK_b\".PRENOT_BANCO_{chk_id}
         OK_SCARICO      :=\"@WORK_b\".OK_SCARICO_BANCO_{chk_id}

///
      AN    \"{motor_code}_S001\"          // <- SENSORE SICUREZZA S1 (0=ALLARME)
      SET
      R     \"DB141_LGK_M\"._{motor_code}.I_ALL_SAFETY_S1
///
      A     \"{motor_code}_PB_ROSSO\"      // <- PULSANTE BLOCCO ROSSO
      R     \"Ist_UT_101-200\"._{motor_code}.BU.INTESTATURA
      R     \"Ist_UT_101-200\"._{next_motor_code}.BU.INTESTATURA
"""

# Generate blocks
for i in range(8):
    chk_id = start_chk + i
    motor_code = f"C{start_odd_motor + i * 2}"
    next_motor_code = f"C{start_odd_motor + i * 2 + 1}"
    bf1 = start_photocell
    bf2 = start_photocell + 1
    bf3 = start_photocell + 2
    
    output = structure_template.format(
        chk_id=chk_id,
        motor_code=motor_code,
        next_motor_code=next_motor_code,
        bf1=bf1,
        bf2=bf2,
        bf3=bf3
    )

    print(output)

    start_photocell += 3
