# This program takes the seconds as input and converts it to proper hours, minutes, and seconds

seconds = int(input("Enter the seconds: "))

hours = seconds // 3600

remaining_seconds = seconds % 3600

minutes = remaining_seconds // 60

final_seconds = remaining_seconds % 60

print(str(seconds), "seconds are same as", str(hours), "Hours", str(minutes), "Minutes and", str(final_seconds), "Seconds")