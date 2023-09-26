name = input("Enter your fullName: ")
idNumber = input("Enter your ID number: ")
exams = [int(input("Enter the mark for your first exam: ")), int(input("Enter the mark for your second exam: ")), int(input("Enter the mark for your third exam: ")), int(input("Enter the mark for your forth exam: ")), int(input("Enter the mark for your fifth exam: ")), int(input("Enter the mark for your sixth exam: ")), int(input("Enter the mark for your seventh exam: "))]

aveMark = round(sum(exams) / 7)

print("Name: ", name, "\nID number: ", idNumber, "\nYour average mark: ", aveMark)