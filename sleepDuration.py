duration_hours = int(input("Enter the amount of time you'll sleep in hours: ")) 
duration_min = int(input("Enter the amount of time you'll sleep in minutes: ")) 
duration_sec = int(input("Enter the amount of time you'll sleep in seconds: ")) 

hour_convert = duration_hours * 3600 
min_convert = duration_min * 60 
total_duration = hour_convert + min_convert + duration_sec 

print(total_duration, "seconds") 