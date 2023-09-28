number_mon = int(input("ENter the amount of months: "))

calculate_year = number_mon // 12
calculate_mon = number_mon % 12

print(calculate_year, "years", "and", calculate_mon, "months")