a = float(input("Enter the coefficient of x in the first equation: "))
b = float(input("Enter the coefficient of y in the first equation: "))
c = float(input("Enter the constant term in the first equation: "))

d = float(input("Enter the coefficient of x in the second equation: "))
e = float(input("Enter the coefficient of y in the second equation: "))
f = float(input("Enter the constant term in the second equation: "))

determinant = a*e - b*d

if determinant == 0:
    print("The system has no unique solution.")
else:
    x = (c*e - b*f) / determinant
    y = (a*f - c*d) / determinant
    print(f"The solution is: x={x:.2f}, y={y:.2f}")