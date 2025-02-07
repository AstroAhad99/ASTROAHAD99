
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
        INSERT INTO TelegramData (message, timestamp) VALUES (?, ?)
    """

    # Run the loop for each incremental value
    for i in range(1, difference + 1):
        index = (prev + i) % MAX_VALUE
        if index == 0:
            index = MAX_VALUE  # Adjust for wrap-around case

        # Construct tag path dynamically based on index
        tagPath = "[default]Logger/Telegram/Telegram {}/12_Message_Conc".format(index)

        # Read the tag value
        message = system.tag.readBlocking(tagPath)
        valueMsg = message[0]      
        msg = valueMsg.value
        
        # Get the current timestamp
        timestamp = system.date.now()
        
        # New Test tagpaths
        tagPath_day = "[default]Logger/Telegram/Telegram {}/5_Day".format(index)
        tagPath_mon = "[default]Logger/Telegram/Telegram {}/4_Month".format(index)
        tagPath_yer = "[default]Logger/Telegram/Telegram {}/3_Year".format(index)
        tagPath_hor = "[default]Logger/Telegram/Telegram {}/7_Hour".format(index)
        tagPath_min = "[default]Logger/Telegram/Telegram {}/8_Minute".format(index)
        tagPath_sec = "[default]Logger/Telegram/Telegram {}/9_Second".format(index)
        
        allpaths = [tagPath_day, tagPath_mon, tagPath_yer, tagPath_hor, tagPath_min, tagPath_sec]
        allvalues = system.tag.readBlocking(allpaths)
        
        valueDay = allvalues[0]      
        day = valueDay.value
        
        valueMon = allvalues[1]      
        mon = valueMon.value
        
        valueYer = allvalues[2]      
        yer = valueYer.value
        
        valueHor = allvalues[3]      
        hor = valueHor.value
        
        valueMen = allvalues[4]      
        men = valueMen.value
        
        valueSec = allvalues[5]      
        sec = valueSec.value
        
        #comDate = str(day+mon+yer+hor+men+sec)
        
        dateObject = system.date.getDate(yer, mon, day)
        dateTimeObject = system.date.setTime(dateObject, hor, men, sec)
        formattedDT = system.date.format(dateTimeObject, "yyyy-MM-dd HH:mm:ss")



        # Insert into database using system.db.runPrepUpdate
        #system.db.runPrepUpdate(query, [msg, timestamp], DATABASE_CONNECTION)
        system.db.runPrepUpdate(query, [msg, formattedDT], DATABASE_CONNECTION)
        
        