triaBase = float(input("Enter the base of the triangle: ")) 
triaHeight = float(input("Enter the height of the traingle: ")) 
areaType = input("Is in centimiter or meter? ") 

area = round(triaBase * triaHeight / 2) 

if areaType == "Centimiter": 
    print(area, "Centimiter squared") 
elif areaType == "Meter": 
    print(area, "Meter squared") 