coPrice = float(input("Enter the cost price of the item: "))
perDiscount = float(input("Enter the percentage discount: "))

diValue = (perDiscount / 100) * coPrice
saPrice = coPrice - diValue

print("Sale price: ", "%.2f"%saPrice)
print("Discount price: ", "%.2f"%diValue)