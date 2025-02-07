
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
        tagPath1 = "[default]Logger/Telegram/Telegram_Original/Telegram {}/3_Log_Conc".format(index)
        tagPath2 = "[default]Logger/Telegram/Telegram_Original/Telegram {}/2_Date_Time".format(index)

        # Read the tag value
        message = system.tag.readBlocking(tagPath1)

        # Get the current timestamp
        timestamp = system.tag.readBlocking(tagPath2)
        
        valueMsg = message[0]
        valueDT = timestamp[0]
#        
        msg = valueMsg.value
        dt = valueDT.value


        # Insert into database using system.db.runPrepUpdate
        system.db.runPrepUpdate(query, [msg, dt], DATABASE_CONNECTION)