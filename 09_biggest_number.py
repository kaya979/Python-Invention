x = 0
y = 0
z = 0

x = input(" Give me 3 numbers, and I will define the biggest: Give me the first number:  ")

y = input("Give me the 2nd number:   ")
z = input("Give me the 3rd number:   ")

print(" your numbers are ", x, y, z)

if (x > y) and (x > z):
    print(x, "is the biggest")
elif (y > z) and (y > x):
    print(y, "is the biggest")
elif (z > x) and (z > y ): 
    print(z, " is the biggest number")