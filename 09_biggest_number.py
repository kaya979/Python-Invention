x = 0
y = 0
z = 0

x = int(input("Enter 3 numbers, and I will return the highest: Give me the first number:  "))

y = int(input("Enter 2nd number:   "))
z = int(input("Enter 3rd number:   "))

print(" Your numbers are ", x, y, z)

if (x >= y) and (x >= z):
    print(x, "is the biggest")
elif (y >= x) and (y >= z):
    print(y, "is the biggest")
elif (z >= x) and (z >= y ): 
    print(z, " is the biggest number")