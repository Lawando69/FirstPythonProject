sphere_rad = float(input("Enter the radius of the sphere: "))
PINUMBER = 3.14159265359

sphere_area = (4 * PINUMBER) * sphere_rad ** 2
sphere_vol = (4 / 3 * PINUMBER) * sphere_rad ** 3 

print("The area of the sphere: ","%.2f"%sphere_area)
print("The volume of the sphere: ","%.2f"%sphere_vol)