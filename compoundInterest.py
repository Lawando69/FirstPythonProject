principle_amount = 10000
compound_per_year = 12
interest_rate = 0.08
number_year = int(input("Enter the number of years the money will be compounded for: "))

total = principle_amount * (1 + interest_rate / compound_per_year) ** (compound_per_year * number_year)

print("The total amount: ", total)