seconds = 14926

hours = seconds // 3600 #These are total hours

seconds_left = seconds % 3600 #These are leftover seconds then used in minutes

minutes = seconds_left // 60 #These are total minutes

final_seconds = seconds % 60 #All seconds consumed by minutes and these are remainings

print(str(seconds) , "seconds is the same as")
print(str(hours) , "hours," , minutes  , "minutes, and" , final_seconds , "seconds")