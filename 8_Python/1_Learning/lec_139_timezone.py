from datetime import datetime, timezone, timedelta

print(datetime.now()) # This is naive time because it does not know about the timezone

print(datetime.now(timezone.utc)) # This gives the time with offset UTC 0

# In program we should always use UTC time

today = datetime.now()
tomorrow = today + timedelta(days=1)
print(today)
print(tomorrow)

print(today.strftime("%d-%m-%Y %H:%M:%S")) #String format time

# To take input from the User to make it parse the time

usertime = input("Enter the time in this format : YYYY-MM-DD: ")
parsetime = datetime.strptime(usertime, "%Y-%m-%d")
print(parsetime)