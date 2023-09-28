mark1 = int(input("Enter the amount for the first mark: "))
mark2 = int(input("Enter the amount for the second mark: "))
mark3 = int(input("Enter the amount for the third mark: "))

totalMark = mark1 + mark2 + mark3
avMark = totalMark / 3

#Prints the average mark in two decimal places
print("The average mark: ", "%.2f"%avMark)