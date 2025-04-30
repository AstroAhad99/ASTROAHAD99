# Python Script to Generate 6 Sets of Banco Structures with Updated Details

# Starting values
start_chk_id = 67
start_c_code = 2101
start_b_code = 75

# Template for Banco
banco_template = """
NETWORK
TITLE = LANCIO BANCO CH{chk_id}: {c1} -> {c2} -> B249 - {b_code}
      A     "@WORK_b".PRENOT_BANCO_{chk_id}// <- Booking Comand
      FP    "FP_CH{chk_id}_BOOK"
      =     "MEM_CH{chk_id}_BOOK"
//*
      CALL  "FC01_Booking_Logic"
         On_Book              :="MEM_CH{chk_id}_BOOK"// <- Booking Comand // -> STATO PRENOTAZIONE TAKE-AWAY BANCO
         Insertion_Point_mm   :=14650.0 // <- Insertion point calculated in mm from the beginning of the collector
         CHK_ID               :={chk_id} // <- Check In Identification Number
         I_DIR_Reverse        :="DB141_LGK_M"._B249.I_SEL_DIR_REV// <- Collector Direction (1 = Reverse)
         Collector_Speed_mm_s :=500.0 // <- Collector Speed to calculate Estimated pph
         Parcel_Length_mm     :=900.0 // <- Parcel length in mm
         Gap_mm               :=400.0 // <- Expected Gap Between Items in mm
         Transfer_win_mm      :=100.0 // <- Transfer window is the space that it takes an item to transfer from chk to the collector
         Parcel_win_mm        :="_CH{chk_id}_ParcelWinmm"// -> The sum of Length + Gap + Transfer win
         Expected_pph         :="_CH{chk_id}_Ex_PPH"// -> Calculated Performance in parcel per hour
         DB_Tracking_Array    :="DB_CHK_TRACK".B249// <--> DB Tracking Array of the collector
         Is_Booked            :="_CH{chk_id}_IsBooked"// <--> This Indicates that a window is successfully booked
///**
      CALL  "FC02_Dispatch_Logic"
         CHK_ID             :={chk_id} // <- Check In Identification Number
         Insertion_Point_mm :=14650.0 // <- Insertion point calculated in mm from the beginning of the collector
         Parcel_win_mm      :="_CH{chk_id}_ParcelWinmm"// -> The sum of Length + Gap + Transfer win
         I_DIR_Reverse      :="DB141_LGK_M"._B249.I_SEL_DIR_REV// <- Collector Direction (1 = Reverse)
         DB_Tracking_Array  :="DB_CHK_TRACK".B249// <--> DB Tracking Array of the collector
         Is_Booked          :="_CH{chk_id}_IsBooked"// <--> This Indicates that a window is successfully booked
         On_Dispatch        :="@WORK_b".OK_SCARICO_BANCO_{chk_id}// <- STATO OK_SCARICO TAKE-AWAY BANCO
///--
      AN    "@WORK_b".OK_SCARICO_BANCO_{chk_id}// <- FOTOCELLULA BF3 FINE NASTRO 2 (1=PRES OBJ)
      FP    "FP_CH{chk_id}_DISPATCH"
      R     "_CH{chk_id}_IsBooked"
//--
      AN    "@WORK_b".PRENOT_BANCO_{chk_id}
      R     "_CH{chk_id}_IsBooked"
"""

# Generate 6 structures
for i in range(6):
    c1 = f"C{start_c_code}"
    c2 = f"C{start_c_code + 1}"
    
    network = banco_template.format(
        chk_id=start_chk_id,
        c1=c1,
        c2=c2,
        b_code=start_b_code
    )

    print(network)

    # Update counters
    start_chk_id += 1
    start_c_code += 2
    start_b_code += 1