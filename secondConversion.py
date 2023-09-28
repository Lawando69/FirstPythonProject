number_sec = int(input("Enter the amount of seconds: "))

calculate_min = number_sec // 60
calculate_sec = number_sec % 60

print(calculate_min, "minutes", "and", calculate_sec, "seconds")
