import math

x1 = float(input("Enter the x-coordinate of first point: "))
y1 = float(input("Enter the y-coordinate of first point: "))
z1 = float(input("Enter the z-coordinate of first point: "))

x2 = float(input("Enter the x-coordinate of second point: "))
y2 = float(input("Enter the y-coordinate of second point: "))
z2 = float(input("Enter the z-coordinate of second point: "))

distance = math.sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2)
print(f"The distance between the two points is: {distance:.2f}")