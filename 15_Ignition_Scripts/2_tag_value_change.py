
    # Define the maximum value as a variable for easy modification
    MAX_VALUE = 10  
    DATABASE_CONNECTION = "TelegramStorage"  # Define database connection name

    # Extract values
    prev = previousValue.value
    curr = currentValue.value

    # Ensure values are within the valid range (1 - MAX_VALUE)
    if prev < 1 or prev > MAX_VALUE or curr < 1 or curr > MAX_VALUE:
        return

    # Calculate difference considering the wrap-around at MAX_VALUE
    if curr >= prev:
        difference = curr - prev
    else:
        difference = (MAX_VALUE - prev) + curr

    # SQL Query to insert data
    query = """
        INSERT INTO TelegramData2 (message, timestamp) VALUES (?, ?)
    """

    # Run the loop for each incremental value
    for i in range(1, difference + 1):
        index = (prev + i) % MAX_VALUE
        if index == 0:
            index = MAX_VALUE  # Adjust for wrap-around case

        # Construct tag path dynamically based on index
        tagPath1 = "[default]Logger/Telegram/Telegram_Original/Telegram {}/5_Day".format(index)
        tagPath2 = "[default]Logger/Telegram/Telegram_Original/Telegram {}/4_Month".format(index)
        tagPath3 = "[default]Logger/Telegram/Telegram_Original/Telegram {}/3_Year".format(index)
        tagPath4 = "[default]Logger/Telegram/Telegram_Original/Telegram {}/7_Hour".format(index)
        tagPath5 = "[default]Logger/Telegram/Telegram_Original/Telegram {}/8_Minute".format(index)
        tagPath6 = "[default]Logger/Telegram/Telegram_Original/Telegram {}/9_Second".format(index)
        
        tagPath7 = "[default]Logger/Telegram/Telegram_Original/Telegram {}/3_Log_Conc".format(index)

        # Read the tag value
        message = system.tag.readBlocking(tagPath7)

        # Get the current timestamp
        day = str(system.tag.readBlocking(tagPath1))
#        mon = str(system.tag.readBlocking(tagPath2))
#        yer = str(system.tag.readBlocking(tagPath3))
#        hor = str(system.tag.readBlocking(tagPath4))
#        mnt = str(system.tag.readBlocking(tagPath5))
#        sec = str(system.tag.readBlocking(tagPath6))
        
        #time = day + mon + yer + hor + mnt + sec
        time = day
        valueMsg = message[0]
#        valueDT = timestamp[0]
#        
        msg = valueMsg.value
#        dt = valueDT.value


        # Insert into database using system.db.runPrepUpdate
        system.db.runPrepUpdate(query, [msg, time], DATABASE_CONNECTION)