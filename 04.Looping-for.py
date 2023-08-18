############################################
#       What is Looping???                 #
#       or How to repeat a task            #
############################################

# What if someone wants you to write from 1 to 100. 
# What if someone asks you to write your name a 1000 times?
# What solution would you come up with?
# Which Python function can help you?
# Writing out 1 - 100 is not efficient. 

# For this Python has 2 kinds of loops to execute a statement multiple times. 

# FOR LOOP
# WHILE LOOP


# For Loop repeats  over a given sequence. 
# example:

# for variable in sequence
#     statements


# this variable:  will update every time the loop is executed
# the sequence:  contains the data over which the looping needs to be done. 

for num in range (0,101):
    print(num)

# range = a Python Function : it takes a starting value and an ending value
# the range will generate a list of numbers beginning with and inclusive of 
# the starting value up to and excluding the ending value. 


for num in range (20):
    print(num)

# if the range holds only one value, it assumes the starting value is 0 and generates a list from there. 
# so range(100) and range(0-100) will give the same result


# There is also a 3rd parameter; the STEP 
# a step is a number by which the index will change every time the loop executes
# by default a step is 1
for num in range(1,11,2):
    print(num)