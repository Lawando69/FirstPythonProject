pounds = float(input("Enter the amount of pounds: "))
conRate = float(input("Enter the conversion rate in percentage: "))

dollars = pounds * conRate / 100

print("The amount of dollars: ", "%.2f"%dollars)